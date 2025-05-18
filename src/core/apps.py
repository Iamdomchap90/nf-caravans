from django.apps import AppConfig
from django.conf import settings


class CoreAppConfig(AppConfig):
    name = "core"
    verbose_name = "Core"

    def ready(self):
        """
        Import cms_has_publish_permission monkeypatch once the app is ready
        """
        is_django_cms_installed = "cms" in settings.INSTALLED_APPS
        if is_django_cms_installed:
            from core.monkeypatches import cms_has_publish_permission  # noqa
