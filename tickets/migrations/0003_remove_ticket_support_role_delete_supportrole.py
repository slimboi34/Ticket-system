# Generated by Django 5.1 on 2024-10-13 17:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0002_supportrole_ticket_support_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="support_role",
        ),
        migrations.DeleteModel(
            name="SupportRole",
        ),
    ]
