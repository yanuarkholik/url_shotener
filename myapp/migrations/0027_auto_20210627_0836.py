# Generated by Django 3.1.7 on 2021-06-27 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20210626_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customurls',
            name='short_url',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
