from plugins.key_stat import cms_plugins


class TestKeyStatPlugin:
    def test_template(self):
        plugin = cms_plugins.KeyStatPlugin()
        assert plugin.render_template == "plugins/key_stat.html"
