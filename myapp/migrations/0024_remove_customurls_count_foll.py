# Generated by Django 3.1.7 on 2021-06-26 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_customurls_count_foll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customurls',
            name='count_foll',
        ),
    ]