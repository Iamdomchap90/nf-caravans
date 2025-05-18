from plugins.people_cards import cms_plugins


class TestPeoplePlugin:
    def test_template(self):
        plugin = cms_plugins.PersonContainerPlugin()
        assert plugin.render_template == "plugins/people.html"
