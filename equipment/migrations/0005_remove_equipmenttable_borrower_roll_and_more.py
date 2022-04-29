# Generated by Django 4.0.4 on 2022-04-23 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0004_rename_borrowerinfo_borrower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmenttable',
            name='borrower_roll',
        ),
        migrations.AddField(
            model_name='equipmenttable',
            name='borrower',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='equipment.borrower'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='borrower',
            name='borrower_roll',
            field=models.CharField(max_length=50),
        ),
    ]
