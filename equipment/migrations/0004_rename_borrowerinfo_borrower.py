# Generated by Django 4.0.4 on 2022-04-22 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_equipmenttable_rename_borrower_borrowerinfo_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BorrowerInfo',
            new_name='Borrower',
        ),
    ]
