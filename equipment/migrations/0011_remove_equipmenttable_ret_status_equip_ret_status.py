# Generated by Django 4.0.4 on 2022-04-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0010_alter_equipmenttable_borrower_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmenttable',
            name='ret_status',
        ),
        migrations.AddField(
            model_name='equip',
            name='ret_status',
            field=models.BooleanField(default=False),
        ),
    ]
