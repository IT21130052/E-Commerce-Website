# Generated by Django 5.0 on 2023-12-20 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0012_alter_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additional_info',
        ),
    ]