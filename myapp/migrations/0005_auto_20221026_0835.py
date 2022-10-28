# Generated by Django 2.1.5 on 2022-10-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20221026_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='flower',
            name='tags',
            field=models.ManyToManyField(to='myapp.Tag'),
        ),
    ]