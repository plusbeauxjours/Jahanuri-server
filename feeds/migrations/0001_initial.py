# Generated by Django 3.0.5 on 2020-05-24 09:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('class_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='classes.ClassOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
