# Generated by Django 3.1.7 on 2021-04-04 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_urls_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urls',
            name='urls',
        ),
    ]
