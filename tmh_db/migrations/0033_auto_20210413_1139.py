# Generated by Django 3.1.5 on 2021-04-13 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0032_structural_residue_opm_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structural_residue',
            name='memprotmd_headgroups',
        ),
        migrations.RemoveField(
            model_name='structural_residue',
            name='memprotmd_tail',
        ),
    ]
