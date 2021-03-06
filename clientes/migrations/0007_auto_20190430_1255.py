# Generated by Django 2.2 on 2019-04-30 12:55

from django.db import migrations


def separar_nome_sobrenome(apps, schema_editor):
    Cliente = apps.get_model('clientes', 'Cliente')
    for cliente in Cliente.objects.all():
        if " " in cliente.nome:
            nome, sobrenome = cliente.nome.split(" ", 1)
            cliente.nome = nome
            cliente.sobrenome = sobrenome
            cliente.save()
        else:
            cliente.sobrenome = " "
            cliente.save()

class Migration(migrations.Migration):


    dependencies = [
        ('clientes', '0006_cliente_sobrenome'),
    ]

    operations = [
        migrations.RunPython(separar_nome_sobrenome),
    ]
