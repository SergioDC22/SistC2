# Generated by Django 3.2.8 on 2022-06-16 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudio', '0007_rename_isestado_impuesto_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impuesto',
            name='estado',
        ),
    ]
