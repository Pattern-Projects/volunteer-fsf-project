# Generated by Django 2.2.6 on 2019-12-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0003_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Amount',
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=100),
        ),
    ]
