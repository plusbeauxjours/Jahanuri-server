# Generated by Django 3.0.5 on 2020-04-26 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200426_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='has_submited_survey',
            new_name='has_submited_check_list',
        ),
    ]
