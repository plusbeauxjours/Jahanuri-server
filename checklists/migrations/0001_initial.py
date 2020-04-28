# Generated by Django 3.0.5 on 2020-04-28 01:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckListQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('elements', models.CharField(blank=True, choices=[('wood', 'Wood'), ('fire', 'Fire'), ('earth', 'Earth'), ('metal', 'Metal'), ('water', 'Water'), ('sanghwa', 'Sanghwa')], max_length=20)),
                ('question', models.CharField(max_length=5000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckListAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('previous_answer', models.BooleanField(default=False)),
                ('later_answer', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklists.CheckListQuestion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
