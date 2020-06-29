# Generated by Django 3.1b1 on 2020-06-29 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checklists', '0003_auto_20200629_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checklistanswer', to=settings.AUTH_USER_MODEL, verbose_name='회원'),
        ),
    ]