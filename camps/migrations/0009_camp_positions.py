# Generated by Django 2.2.6 on 2019-11-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0008_remove_camp_positions'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='positions',
            field=models.IntegerField(null=True),
        ),
    ]
