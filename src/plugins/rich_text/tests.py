import pytest

from plugins.rich_text import cms_plugins, models


class TestRichTextPlugin:
    def test_template(self):
        plugin = cms_plugins.RichTextPlugin()
        assert plugin.render_template == "plugins/rich_text.html"


@pytest.mark.django_db
class TestRichTextModel:
    @pytest.fixture
    def plugin_instance(self):
        return models.RichText(
            content="<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Pellentesque pellentesque odio vel eros tempor bibendum."
            "Sed consequat cursus sapien vel ultricies."
            "Duis lorem lorem, ornare.</p>"
        )

    def test_str(self, plugin_instance):
        instance = plugin_instance
        assert str(instance) == instance.excerpt

    def test_strip_tags(self, plugin_instance):
        instance = plugin_instance

        assert "<p>" not in instance.plain_text

    def test_excerpt(self, plugin_instance):
        instance = plugin_instance
        word_count = len(instance.excerpt.split())
        assert word_count <= 20
