# Generated by Django 2.1.7 on 2019-03-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0012_tmh_tmh_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmh',
            name='tmh_id',
            field=models.TextField(),
        ),
    ]
