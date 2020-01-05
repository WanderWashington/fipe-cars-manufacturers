# Generated by Django 2.1.4 on 2020-01-05 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fipe_api', '0004_auto_20200104_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='manuf_car', to='fipe_api.Marca'),
        ),
    ]
