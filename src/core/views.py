from django.contrib.sites.models import Site
from django.shortcuts import redirect, render
from django.templatetags.static import static

from cms.models import Page, TreeNode


def favicon(request):
    """
    Redirects to our favicon.ico
    """
    return redirect(static("meta/favicon.ico"))


def robots(request):
    """
    Renders our robots.txt
    """
    return render(request, "_root/robots.txt", content_type="text/plain")


def google_verification(request):
    """
    Renders our verification file for google
    """
    return render(request, "_root/google33b1735040ebbe58.html")


def sitemap(request):
    """
    Simple view to show an HTML sitemap
    """
    site = Site.objects.get_current()
    pages = (
        Page.objects.public()
        .published(site=site)
        .order_by("node__path")
        .filter(in_navigation=True)
        .distinct()
    )

    nodes = [page.node for page in pages.select_related("node")]
    annotated_nodes = TreeNode.get_annotated_list_qs(nodes)
    annotated_pages = [(pages[x], annotated_nodes[x][1]) for x in range(0, len(nodes))]

    return render(request, "sitemap.html", {"pages": annotated_pages})
