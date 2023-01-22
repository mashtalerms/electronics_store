# Generated by Django 4.1.5 on 2023-01-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_chain', '0005_remove_dealership_contacts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='address',
        ),
        migrations.AddField(
            model_name='contacts',
            name='address',
            field=models.ManyToManyField(to='e_chain.address'),
        ),
    ]
