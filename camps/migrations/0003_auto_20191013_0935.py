# Generated by Django 2.2.6 on 2019-10-13 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0002_auto_20191010_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='extra_host_country_fee',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='extra_host_country_fee_currency',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='image',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='positions',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='positions_female',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='positions_male',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='tag',
        ),
    ]
