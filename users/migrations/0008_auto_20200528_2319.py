# Generated by Django 3.0.5 on 2020-05-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_appleid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='appleId',
            new_name='apple_id',
        ),
        migrations.AddField(
            model_name='user',
            name='kakao_id',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]