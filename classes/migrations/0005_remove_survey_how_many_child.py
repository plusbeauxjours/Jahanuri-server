# Generated by Django 3.0.5 on 2020-05-27 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20200527_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='how_many_child',
        ),
    ]
