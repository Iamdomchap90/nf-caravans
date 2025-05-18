from plugins.video import cms_plugins, models


class TestVideoPlugin:
    def test_template(self):
        plugin = cms_plugins.ContentWidthVideoPlugin()
        assert plugin.render_template == "plugins/video.html"


class TestVideoModel:
    def test_str(self):
        obj = models.Video(title="Man helping cat")
        assert str(obj) == "Video: Man helping cat"
