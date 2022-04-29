# Generated by Django 4.0.4 on 2022-04-22 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_roll', models.CharField(max_length=50)),
                ('equip_id', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('ret_date', models.DateTimeField(verbose_name='date returned')),
            ],
        ),
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equip_name', models.CharField(max_length=100)),
                ('return_status', models.BooleanField(default=False)),
                ('equip_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.maintable')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_name', models.CharField(max_length=50)),
                ('hostelNo', models.IntegerField()),
                ('contactNo', models.IntegerField(max_length=10)),
                ('borrower_roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.maintable')),
            ],
        ),
    ]
