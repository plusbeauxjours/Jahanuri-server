# Generated by Django 3.0.5 on 2020-05-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_habit_check_list_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
