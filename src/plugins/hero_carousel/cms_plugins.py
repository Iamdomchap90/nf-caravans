from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.hero_carousel import models


class ImageInlineAdmin(admin.StackedInline):
    model = models.Image
    max_num = 5
    extra = 5


@plugin_pool.register_plugin
class HeroCarouselPlugin(CMSPluginBase):
    """
    CMS plugin for the Hero Carousel model
    """

    model = models.HeroCarousel
    name = "Hero Carousel"
    render_template = "plugins/hero_carousel.html"
    inlines = [ImageInlineAdmin]
