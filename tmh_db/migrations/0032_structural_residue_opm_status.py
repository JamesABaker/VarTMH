# Generated by Django 3.1.5 on 2021-04-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0031_auto_20201106_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='structural_residue',
            name='opm_status',
            field=models.CharField(default='', max_length=10),
        ),
    ]
