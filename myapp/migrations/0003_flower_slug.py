# Generated by Django 2.1.5 on 2022-10-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_flower_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
