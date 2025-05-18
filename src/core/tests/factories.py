from django.utils import timezone

import factory


class FilerImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "filer.Image"


class FilerFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "filer.File"


class CategoryFactoryMixin(factory.django.DjangoModelFactory):
    """
    Core factory for creating categories. Adds a name and slug field. Simply inherit this class and
    define your model's Meta class with the relevant category model.
    """

    name = factory.Faker("sentence", nb_words=10)
    slug = factory.Faker("uuid4")


class PublishingFactoryMixin(factory.django.DjangoModelFactory):
    """
    Core factory for creating models with publishing fields. Adds is_published and publish_at
    fields. By default will mark items as published
    """

    is_published = True
    publish_at = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())


class TaggableFactoryMixin(factory.django.DjangoModelFactory):
    """
    Core factory for creating models with tags. Adds a tags post-generation method. Allows you to
    pass in a list of tags to add to the model instance.
    """

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)


class ContentModelFactoryMixin(PublishingFactoryMixin, TaggableFactoryMixin):
    """
    Core factory for creating content models. Adds a title, slug, and category field. Inherit this
    class and define your model's Meta class with the relevant model.
    """

    slug = factory.Faker("uuid4")  # Ensure unique slugs across everything
