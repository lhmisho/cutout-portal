# Generated by Django 3.2.2 on 2021-06-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20210602_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='addons',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requirement',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
