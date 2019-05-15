# Generated by Django 2.2 on 2019-05-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0003_auto_20190515_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structure',
            name='pdb_id',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='structure',
            unique_together={('pdb_id', 'uniprot_protein')},
        ),
    ]
