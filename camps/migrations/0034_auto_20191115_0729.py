# Generated by Django 2.2.6 on 2019-11-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0033_auto_20191115_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='camp',
            name='start_date',
            field=models.DateField(),
        ),
    ]
