# Generated by Django 3.1.7 on 2021-06-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_customurls_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customurls',
            name='domain',
            field=models.CharField(choices=[(1, 'singkat.in'), (2, 'hahahihi.in'), (3, 'pendek.aja')], default='1', max_length=30),
        ),
    ]
