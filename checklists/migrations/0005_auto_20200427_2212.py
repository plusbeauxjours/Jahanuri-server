# Generated by Django 3.0.5 on 2020-04-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0004_auto_20200427_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistanswer',
            name='later_answer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='checklistanswer',
            name='previous_answer',
            field=models.BooleanField(default=False),
        ),
    ]
