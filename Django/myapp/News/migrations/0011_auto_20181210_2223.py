# Generated by Django 2.1.2 on 2018-12-10 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0010_auto_20181210_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataregistro',
            old_name='telefone',
            new_name='tel',
        ),
    ]
