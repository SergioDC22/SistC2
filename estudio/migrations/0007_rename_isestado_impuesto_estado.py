# Generated by Django 3.2.8 on 2022-06-16 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudio', '0006_auto_20220615_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impuesto',
            old_name='isestado',
            new_name='estado',
        ),
    ]