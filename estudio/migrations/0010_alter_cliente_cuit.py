# Generated by Django 4.0.5 on 2022-06-30 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudio', '0009_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='CUIT',
            field=models.PositiveIntegerField(),
        ),
    ]
