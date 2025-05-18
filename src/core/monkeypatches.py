from typing import Callable
from urllib.parse import quote

from django.conf import settings
from django.contrib.auth.views import redirect_to_login

from cms.cms_toolbars import PageToolbar
from cms.page_rendering import _handle_no_page
from cms.utils import decorators, get_current_site, page_permissions
from cms.utils.page_permissions import user_can_view_page


def cms_has_publish_permission() -> Callable:
    """
    Monkeypatch to fix the lack of the publish button for static placeholders
    that are not on CMS pages
    """

    def has_publish_permission(self: PageToolbar) -> bool:
        is_has_publish_permission = False

        is_page_model_available = self.page is not None
        if is_page_model_available:
            is_has_publish_permission = page_permissions.user_can_publish_page(
                self.request.user,
                page=self.page,
                site=self.current_site,
            )

        is_need_to_check_dirty_static_placeholders_perms = (
            is_has_publish_permission or not is_page_model_available
        ) and self.statics
        if is_need_to_check_dirty_static_placeholders_perms:
            is_has_publish_permission = all(
                sp.has_publish_permission(self.request) for sp in self.dirty_statics
            )

        return is_has_publish_permission

    return has_publish_permission


PageToolbar.has_publish_permission = cms_has_publish_permission()


def _cms_perms():
    def cms_perms(func):
        def inner(request, *args, **kwargs):
            page = request.current_page
            if page:
                if page.login_required and not request.user.is_authenticated:
                    return redirect_to_login(quote(request.get_full_path()), settings.LOGIN_URL)
                site = get_current_site()
                if not user_can_view_page(request.user, page, site):
                    return _handle_no_page(request)
            return func(request, *args, **kwargs)

        inner.__module__ = func.__module__
        inner.__doc__ = func.__doc__

        if hasattr(func, "view_class"):
            inner.view_class = func.view_class
        if hasattr(func, "__name__"):
            inner.__name__ = func.__name__
        elif hasattr(func, "__class__"):
            inner.__name__ = func.__class__.__name__

        if getattr(func, "csrf_exempt", False):
            # view has set csrf_exempt flag
            # so pass it down to the decorator.
            inner.csrf_exempt = True
        return inner

    return cms_perms


decorators.cms_perms = _cms_perms()
