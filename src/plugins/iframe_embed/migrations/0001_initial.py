# Generated by Django 5.2.1 on 2025-05-21 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cms", "0041_alter_pageurl_unique_together_pageurl_site_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="IframeEmbed",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="%(app_label)s_%(class)s",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                ("snippet", models.TextField()),
            ],
            bases=("cms.cmsplugin",),
        ),
    ]
