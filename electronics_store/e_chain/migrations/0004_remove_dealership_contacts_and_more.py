# Generated by Django 4.1.5 on 2023-01-19 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_chain', '0003_remove_dealership_contacts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealership',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='dealership',
            name='products',
        ),
        migrations.RemoveField(
            model_name='dealership',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='products',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='entrepreneur',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='entrepreneur',
            name='products',
        ),
        migrations.RemoveField(
            model_name='entrepreneur',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='factory',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='factory',
            name='products',
        ),
        migrations.RemoveField(
            model_name='factory',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='retail',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='retail',
            name='products',
        ),
        migrations.RemoveField(
            model_name='retail',
            name='staff',
        ),
        migrations.AddField(
            model_name='dealership',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.contacts'),
        ),
        migrations.AddField(
            model_name='dealership',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.products'),
        ),
        migrations.AddField(
            model_name='dealership',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.staff'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.contacts'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.products'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.staff'),
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.contacts'),
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.products'),
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.staff'),
        ),
        migrations.AddField(
            model_name='factory',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.contacts'),
        ),
        migrations.AddField(
            model_name='factory',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.products'),
        ),
        migrations.AddField(
            model_name='factory',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.staff'),
        ),
        migrations.AddField(
            model_name='retail',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.contacts'),
        ),
        migrations.AddField(
            model_name='retail',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.products'),
        ),
        migrations.AddField(
            model_name='retail',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_chain.staff'),
        ),
    ]
