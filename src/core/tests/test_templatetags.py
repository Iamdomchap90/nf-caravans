from django.core.paginator import Paginator
from django.test import RequestFactory, override_settings
from django.utils import timezone

import pytest

from events.tests.factories import EventFactory

from ..templatetags.google_tag_manager import google_tag_manager
from ..templatetags.seo import generate_canonical_url
from ..templatetags.show_pagination import get_pagination_context
from ..templatetags.thumbnail_position import thumbnail_bg_position


class TestGoogleTagManager:
    @override_settings(GTM_ID="")
    def test_gtm_none(self):
        """
        Test that the google tag manager returns empty if it is not configured
        """

        result = google_tag_manager()
        assert "window,document,'script','dataLayer',''" not in result

    def test_javascript_true(self):
        """
        Test the js is present in base html the gtm script if gtm is set
        """

        result = google_tag_manager(javascript=True)
        assert "<script>" in result
        assert "window,document,'script','dataLayer','test_id'" in result

    def test_javascript_false(self):
        """
        Test the js is not present in base html the gtm script if gtm is set
        """

        result = google_tag_manager(javascript=False)
        assert "<noscript>" in result
        assert "https://www.googletagmanager.com/ns.html?id=test_id" in result


class TestThumbnail:
    """
    Test the thumbnail position function
    """

    def test_no_subject_location(self):
        """
        Test center is returned if no subject location given
        """

        assert thumbnail_bg_position(None, None, None) == "center"

    def test_position_return(self):
        """
        Test the correct position is returned
        """

        assert thumbnail_bg_position("600, 600", 600, 600) == "100.0% 100.0%"

    def test_zero_divison_catch(self):
        """
        Test the ZeroDivisionError catch
        """

        assert thumbnail_bg_position("0, 0", 0, 0) == "center"


@pytest.mark.django_db
class TestGetPaginationContext:
    def test_pagination_single_page(self):
        events = EventFactory.create_batch(5)
        paginator = Paginator(events, 9)
        page = paginator.get_page(0)
        request = RequestFactory().get("/fake-url/")

        context = get_pagination_context(page, request)

        assert context["obj_list"] == page
        assert context["visible_pages"] == []
        assert context["show_start_dots"] is False
        assert context["show_end_dots"] is False

    def test_pagination_multiple_pages(self):
        events = EventFactory.create_batch(
            90, publish_at=timezone.now() - timezone.timedelta(days=14)
        )
        paginator = Paginator(events, 9)
        page = paginator.get_page(1)
        request = RequestFactory().get("/fake-url/")

        context = get_pagination_context(page, request)

        assert context["obj_list"] == page
        assert context["visible_pages"] != []
        assert context["show_start_dots"] is False
        assert context["show_end_dots"] is True


class TestGenerateCanonicalUrl:
    def test_no_request_in_context(self):
        context = {}
        result = generate_canonical_url(context)

        assert result == ""

    def test_canonical_no_query_params(self, rf):
        context = {"request": rf.get("/path/")}

        result = generate_canonical_url(context)

        assert result == "http://testserver/path/"

    def test_canonical_page_1(self, rf):
        context = {"request": rf.get("/path/?page=1")}

        result = generate_canonical_url(context)

        assert result == "http://testserver/path/"

    def test_canonical_page_2(self, rf):
        context = {"request": rf.get("/path/?page=2")}

        result = generate_canonical_url(context)

        assert result == "http://testserver/path/?page=2"

    def test_canonical_page_1_and_others(self, rf):
        context = {"request": rf.get("/path/?page=1&param=value")}

        result = generate_canonical_url(context)

        assert result == "http://testserver/path/"

    def test_canonical_page_2_and_others(self, rf):
        context = {"request": rf.get("/path/?page=2&param=value")}

        result = generate_canonical_url(context)

        assert result == "http://testserver/path/?page=2"

    def test_canonical_query_params(self, rf):
        context = {"request": rf.get("/our-impact/our-stories/?search=invictus+games")}

        result = generate_canonical_url(context)

        assert result == "http://testserver/our-impact/our-stories/"
