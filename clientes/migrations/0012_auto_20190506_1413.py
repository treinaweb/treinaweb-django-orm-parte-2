# Generated by Django 2.2 on 2019-05-06 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_auto_20190506_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['-nome']},
        ),
    ]