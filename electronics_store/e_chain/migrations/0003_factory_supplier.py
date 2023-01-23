# Generated by Django 4.1.5 on 2023-01-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_chain', '0002_remove_dealership_supplier_dealership_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='supplier',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Завод'), (2, 'Дистрибьютор'), (3, 'Дилерский центр'), (4, 'Крупная розничная сеть'), (5, 'Индивидуальный предприниматель')], default=1, verbose_name='Поставщик'),
        ),
    ]
