# Generated by Django 3.2 on 2024-09-09 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0002_produto_codigo'),
        ('clientes', '0001_initial'),
        ('vendedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_venda', models.DateField()),
                ('nf', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota Fiscal')),
                ('unidade', models.CharField(max_length=20)),
                ('quantidade', models.PositiveIntegerField()),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Valor Unitário')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Valor Total')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedores.vendedor')),
            ],
            options={
                'ordering': ('-data_da_venda',),
            },
        ),
    ]
