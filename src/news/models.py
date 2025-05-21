from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager

from core.mixins.models import TimestampMixin


class Category(TimestampMixin):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(
        to="people.Person",
        null=True,
        on_delete=models.SET_NULL,
        related_name="articles",
    )
    tags = TaggableManager(related_name="articles")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="articles")

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"slug": self.slug})
