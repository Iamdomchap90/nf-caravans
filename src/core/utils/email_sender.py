import re

from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.template import TemplateDoesNotExist, engines
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags


def extract_body_content(template_content, context):
    django_engine = engines["django"]

    # endblock pattern could include the block name at the end so
    # " %}" is omitted
    pattern = r"{% block body %}(.*?)\{% endblock %}"
    body_content = re.search(pattern, template_content, re.DOTALL).group(1).strip()

    return django_engine.from_string(body_content).render(context)


def send_email_from_template(
    to,
    email_subject: str,
    html_template: str,
    email_sent_attr: str,
    text_template: str = None,
    pk: int = None,
    model_class: object = None,
    scheme: str = "",
    host: str = "",
):
    """
    A core template method which sends an email given the following parameters:
        obj: Usually set as self, but is the instance of the model you are using
        to: The recipient of the mail
        html_template: this is the path to the html version of the template
        email_sent_attr: field name to be set to true upon successful sending of email.
        pk: The model instance's pk to be pulled through into the email templates.
        model_class: The model class to be pulled through into the email templates.
        host: The site's host domain to be pulled through into the email templates
            for correct image url.
    """
    context = {
        "subject": email_subject,
        "scheme": scheme,
        "host": host,
    }
    instance = None
    if model_class and pk:
        instance = model_class.objects.get(pk=pk)
        context = {"obj": instance, "model": model_class, **context}

    try:
        template = get_template(html_template)
    except TemplateDoesNotExist:
        raise Exception(f"The template {html_template} does not exist.")

    raw_html_content = template.template.source

    if text_template:
        txt_result = render_to_string(text_template, context=context)
    else:
        html_content = extract_body_content(raw_html_content, context)
        txt_result = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=context["subject"],
        body=txt_result,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to,
    )

    html_result = render_to_string(html_template, context=context)
    email.attach_alternative(
        content=html_result,
        mimetype="text/html",
    )

    response = email.send()
    if response and email_sent_attr and hasattr(model_class, email_sent_attr) and instance:
        setattr(instance, email_sent_attr, True)
        instance.save()
