# Generated by Django 3.1.7 on 2021-06-24 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_urls_short_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customurls',
            old_name='user',
            new_name='user_custom',
        ),
        migrations.RenameField(
            model_name='urls',
            old_name='user',
            new_name='user_url',
        ),
    ]