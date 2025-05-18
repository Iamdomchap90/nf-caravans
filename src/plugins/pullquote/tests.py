from plugins.pullquote import cms_plugins, models


class TestPullQuotePlugin:
    def test_template(self):
        """
        Test that the template of the plugin is correct
        """
        plugin = cms_plugins.PullQuotePlugin()
        assert plugin.render_template == "plugins/pullquote.html"


class TestPullQuoteModel:
    def test_str(self):
        obj = models.PullQuote(pk=1)
        assert str(obj) == "Pull quote 1"
