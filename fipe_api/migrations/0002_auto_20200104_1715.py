# Generated by Django 2.1.4 on 2020-01-04 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fipe_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marcas',
            new_name='Marca',
        ),
        migrations.RenameModel(
            old_name='Veiculos',
            new_name='Veiculo',
        ),
    ]
