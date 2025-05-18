import pytest

from core.mixins.models import FileMixin, VideoURLMixin


class TestVideoURLMixin:
    class DummyVideoURLMixin(VideoURLMixin):
        pass

    @pytest.fixture
    def video_url_mixin(self):
        mixin = self.DummyVideoURLMixin()
        mixin.youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=43"
        mixin.alternate_url = "https://alternate.com"
        return mixin

    def test_youtube_video_url(self, video_url_mixin):
        expected_url = "https://www.youtube.com/embed/dQw4w9WgXcQ?rel=0&autoplay=1&start=43"
        assert video_url_mixin.youtube_video_url() == expected_url

    def test_get_absolute_url_youtube(self, video_url_mixin):
        assert video_url_mixin.get_absolute_url() == video_url_mixin.youtube_video_url()

    def test_get_absolute_url_alternate(self, video_url_mixin):
        video_url_mixin.youtube_url = None
        assert video_url_mixin.get_absolute_url() == video_url_mixin.alternate_url


class TestFileMixin:
    class DummyFileMixin(FileMixin):
        pass

    @pytest.fixture
    def file_mixin(self, file_instance):
        return self.DummyFileMixin(file=file_instance)

    def test_file_url(self, file_mixin):
        assert file_mixin.file_url == "/media/test_file.pdf"

    def test_file_extension(self, file_mixin):
        assert file_mixin.file_extension == "pdf"

    def test_file_size(self, file_mixin):
        assert file_mixin.file_size == {"value": 4.0, "suffix": "b"}
