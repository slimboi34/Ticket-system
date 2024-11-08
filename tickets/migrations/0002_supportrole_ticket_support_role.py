# Generated by Django 5.1 on 2024-10-13 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SupportRole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("commercial", "Commercial"),
                            ("technical_support", "Technical Support"),
                            ("legal_support", "Legal Support"),
                            ("second_line_support", "2nd Line Support"),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="ticket",
            name="support_role",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tickets",
                to="tickets.supportrole",
            ),
        ),
    ]
