# Generated by Django 4.0.5 on 2022-07-07 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudio', '0012_alter_cliente_cuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='isEstado',
            field=models.BooleanField(default=1),
        ),
    ]
