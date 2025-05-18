from plugins.featured_cta import cms_plugins, models


class TestFeaturedCTAPlugin:
    def test_template(self):
        plugin = cms_plugins.FeaturedCTAPlugin()
        assert plugin.render_template == "plugins/featured_cta.html"


class TestFeaturedCTAModel:
    def test_str(self):
        obj = models.FeaturedCTA(title="This CTA is featured")
        assert str(obj) == "Featured CTA: This CTA is featured"
