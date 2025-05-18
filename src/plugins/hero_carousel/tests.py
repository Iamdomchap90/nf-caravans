from plugins.hero_carousel import cms_plugins


class HeroPluginTests:
    def test_template(self):
        plugin = cms_plugins.HeroCarouselPlugin()
        assert plugin.render_template == "plugins/hero_carousel.html"
