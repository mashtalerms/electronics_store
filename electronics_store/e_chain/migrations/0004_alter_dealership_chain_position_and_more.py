# Generated by Django 4.1.5 on 2023-01-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_chain', '0003_dealership_chain_position_distributor_chain_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealership',
            name='chain_position',
            field=models.SmallIntegerField(null=True, verbose_name='Уровень иерархии'),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='supplier',
            field=models.PositiveSmallIntegerField(choices=[(-1, ''), (0, 'Завод'), (1, 'Дистрибьютор'), (2, 'Дилерский центр'), (3, 'Крупная розничная сеть'), (4, 'Индивидуальный предприниматель')], null=True, verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='chain_position',
            field=models.SmallIntegerField(null=True, verbose_name='Уровень иерархии'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='supplier',
            field=models.PositiveSmallIntegerField(choices=[(-1, ''), (0, 'Завод'), (1, 'Дистрибьютор'), (2, 'Дилерский центр'), (3, 'Крупная розничная сеть'), (4, 'Индивидуальный предприниматель')], null=True, verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='entrepreneur',
            name='chain_position',
            field=models.SmallIntegerField(null=True, verbose_name='Уровень иерархии'),
        ),
        migrations.AlterField(
            model_name='entrepreneur',
            name='supplier',
            field=models.PositiveSmallIntegerField(choices=[(-1, ''), (0, 'Завод'), (1, 'Дистрибьютор'), (2, 'Дилерский центр'), (3, 'Крупная розничная сеть'), (4, 'Индивидуальный предприниматель')], null=True, verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='chain_position',
            field=models.SmallIntegerField(null=True, verbose_name='Уровень иерархии'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='supplier',
            field=models.PositiveSmallIntegerField(choices=[(-1, ''), (0, 'Завод'), (1, 'Дистрибьютор'), (2, 'Дилерский центр'), (3, 'Крупная розничная сеть'), (4, 'Индивидуальный предприниматель')], null=True, verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='retail',
            name='chain_position',
            field=models.SmallIntegerField(null=True, verbose_name='Уровень иерархии'),
        ),
        migrations.AlterField(
            model_name='retail',
            name='supplier',
            field=models.PositiveSmallIntegerField(choices=[(-1, ''), (0, 'Завод'), (1, 'Дистрибьютор'), (2, 'Дилерский центр'), (3, 'Крупная розничная сеть'), (4, 'Индивидуальный предприниматель')], null=True, verbose_name='Поставщик'),
        ),
    ]
