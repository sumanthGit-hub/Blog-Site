# Generated by Django 3.0.1 on 2020-08-06 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(choices=[('Jr Developer', 'Jr Developer'), ('Sr Developer', 'Sr Developer'), ('Accountant', 'Accountant'), ('Sales Manager', 'Sales Manager')], max_length=50),
        ),
    ]