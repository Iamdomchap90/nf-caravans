from plugins.iframe_embed import cms_plugins, models


class TestIframeEmbedPlugin:
    def test_template(self):
        plugin = cms_plugins.IframeEmbedPlugin()
        assert plugin.render_template == "plugins/iframe_embed.html"


class TestIframeEmbedModel:
    def test_str(self):
        obj = models.IframeEmbed(pk=1)
        assert str(obj) == "Iframe Embed 1"
