# Generated by Django 4.0.4 on 2022-04-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0017_remove_equipmenttable_ret_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='equip',
            name='a',
            field=models.IntegerField(default=1),
        ),
    ]
