# Generated by Django 2.1.7 on 2019-03-27 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0017_database_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='protein',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
