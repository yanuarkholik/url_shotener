# Generated by Django 3.1.7 on 2021-06-24 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20210624_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customurls',
            old_name='user_custom',
            new_name='user',
        ),
    ]
