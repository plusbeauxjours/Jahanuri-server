# Generated by Django 3.0.5 on 2020-05-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20200517_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='amino',
            new_name='amino_evening',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='saeng_sik',
            new_name='amino_morning',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='sangi_so',
            new_name='amino_noon',
        ),
        migrations.RemoveField(
            model_name='report',
            name='jeun_hae_jil_time',
        ),
        migrations.AddField(
            model_name='report',
            name='saeng_sik_evening',
            field=models.CharField(choices=[('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening')], default='morning', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='saeng_sik_morning',
            field=models.CharField(choices=[('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening')], default='morning', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='saeng_sik_noon',
            field=models.CharField(choices=[('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening')], default='morning', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='sangi_so_evening',
            field=models.CharField(choices=[('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening')], default='morning', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='sangi_so_morning',
            field=models.CharField(choices=[('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening')], default='morning', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='sangi_so_noon',
            field=models.CharField(choices=[('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening')], default='morning', max_length=200),
        ),
    ]
