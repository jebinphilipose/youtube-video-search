# Generated by Django 3.1.2 on 2020-10-12 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201011_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='search_query',
            field=models.CharField(default='music', max_length=500),
            preserve_default=False,
        ),
    ]