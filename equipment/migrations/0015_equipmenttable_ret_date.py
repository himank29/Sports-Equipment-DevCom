# Generated by Django 4.0.4 on 2022-04-25 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0014_remove_equipmenttable_ret_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmenttable',
            name='ret_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 25, 11, 39, 11, 663211), verbose_name='date returned'),
        ),
    ]
