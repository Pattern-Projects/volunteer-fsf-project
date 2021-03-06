# Generated by Django 2.2.6 on 2019-11-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0035_auto_20191115_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='continent',
            field=models.CharField(default='Europe', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camp',
            name='region',
            field=models.CharField(default='Wesht', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='camp',
            name='positions',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='camp',
            name='positions_female',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='camp',
            name='positions_male',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='camp',
            name='positions_other',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
