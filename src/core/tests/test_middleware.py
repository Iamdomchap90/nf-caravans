from django.core.exceptions import MiddlewareNotUsed
from django.http import HttpResponse
from django.test import RequestFactory

import pytest

from core import middleware


class TestDenyIndexMiddleware:
    def get_response(self, request):
        """
        Helper function used in init
        """
        return HttpResponse()

    def test_init_raises_error_live(self):
        """
        Test that middleware not used in live environment
        """
        with pytest.raises(MiddlewareNotUsed):
            middleware.DenyIndexMiddleware(get_response=self.get_response)

    def test_call(self, settings):
        """
        Test call adds noindex header
        :return:
        """
        settings.DEBUG = True

        request = RequestFactory().get("/")
        instance = middleware.DenyIndexMiddleware(get_response=self.get_response)
        response = instance(request=request)

        assert response["X-Robots-Tag"] == "noindex"
