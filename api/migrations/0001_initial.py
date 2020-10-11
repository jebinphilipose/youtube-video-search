# Generated by Django 3.1.2 on 2020-10-11 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('published_at', models.DateTimeField(db_index=True)),
                ('description', models.TextField(blank=True, max_length=5000)),
                ('thumbnail_url', models.URLField()),
            ],
        ),
    ]