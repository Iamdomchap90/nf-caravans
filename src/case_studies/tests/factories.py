import factory

from case_studies.models import CaseStudy, Category
from core.tests.factories import CategoryFactoryMixin, PublishingFactoryMixin


class CategoryFactory(CategoryFactoryMixin):
    class Meta:
        model = Category


class CaseStudyFactory(PublishingFactoryMixin):
    title = factory.Faker("word")
    slug = factory.Faker("uuid4")
    category = factory.SubFactory(CategoryFactory)
    description = factory.Faker("sentence")

    class Meta:
        model = CaseStudy
