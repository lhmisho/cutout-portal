# Generated by Django 3.2.2 on 2021-06-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_quotation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruction',
            name='addons',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='requirements',
        ),
        migrations.AddField(
            model_name='instruction',
            name='addon',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='instruction',
            name='requirement',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
