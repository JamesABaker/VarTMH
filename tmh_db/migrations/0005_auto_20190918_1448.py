# Generated by Django 2.2.5 on 2019-09-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0004_auto_20190828_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structure',
            name='pdb_id',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]
