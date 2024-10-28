# Generated by Django 5.1.2 on 2024-10-18 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_order_settlement_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='settlement_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='store.settlementrequest'),
        ),
    ]