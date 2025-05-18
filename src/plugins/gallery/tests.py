from plugins.gallery import cms_plugins


class TestGalleryPlugins:
    def test_parent_template(self):
        plugin = cms_plugins.GalleryBlockPlugin()
        assert plugin.render_template == "plugins/gallery/container.html"

    def test_child_template(self):
        plugin = cms_plugins.GalleryImagePlugin()
        assert plugin.render_template == "plugins/gallery/item.html"
