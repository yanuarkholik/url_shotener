# Generated by Django 3.1.7 on 2021-06-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_auto_20210627_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='images/default.jpg/', upload_to='upload'),
        ),
    ]
