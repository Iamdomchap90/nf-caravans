# import pytest

# from core import views

# pytestmark = pytest.mark.django_db


# class TestCoreViews:
#     """
#     Tests for the views in the core module
#     """

#     def test_favicon(self, rf):
#         """
#         Test the favicon view returns the correct response
#         """

#         request = rf.get("meta/favicon.ico")
#         response = views.favicon(request)

#         # assert for 302 as it's a redirect
#         assert response.status_code == 302

#     def test_robots(self, rf):
#         """
#         Test the robots view returns the correct response
#         """

#         request = rf.get("_root/robots.txt")
#         response = views.robots(request)

#         assert response.status_code == 200
#         assert response["content-type"] == "text/plain"

#     def test_google_verification(self, rf):
#         """
#         Test the google_verification view returns the correct response
#         """

#         request = rf.get("_root/google33b1735040ebbe58.html")
#         response = views.google_verification(request)

#         assert response.status_code == 200
#         assert "google33b1735040ebbe58.html" in str(response.content)
