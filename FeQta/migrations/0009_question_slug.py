# Generated by Django 2.0.7 on 2018-08-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeQta', '0008_auto_20180818_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
