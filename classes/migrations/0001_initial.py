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
            name='ClassOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField(blank=True, null=True, unique=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('saeng_sik', models.CharField(choices=[('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening')], default='morning', max_length=200)),
                ('amino', models.CharField(choices=[('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening')], default='morning', max_length=200)),
                ('sangi_so', models.CharField(choices=[('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening')], default='morning', max_length=200)),
                ('jeun_hae_jil', models.BooleanField(default=False)),
                ('jeun_hae_jil_time', models.TimeField()),
                ('meal', models.CharField(max_length=1000)),
                ('meal_check', models.CharField(max_length=1000)),
                ('sleeping', models.CharField(max_length=1000)),
                ('stool', models.CharField(max_length=1000)),
                ('hot_grain', models.CharField(max_length=1000)),
                ('hot_water', models.CharField(max_length=1000)),
                ('strolling', models.CharField(max_length=1000)),
                ('workout', models.CharField(max_length=1000)),
                ('lecture', models.CharField(max_length=1000)),
                ('etc', models.CharField(max_length=1000)),
                ('diary', models.CharField(max_length=5000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReportCover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('report_type', models.CharField(choices=[('body study', 'Body Study'), ('etc', 'Etc')], default='body study', max_length=200)),
                ('class_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='classes.ClassOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
