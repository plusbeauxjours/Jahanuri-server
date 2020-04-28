# Generated by Django 3.0.5 on 2020-04-28 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0003_auto_20200428_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_set', to='checklists.CheckListQuestion'),
        ),
    ]
