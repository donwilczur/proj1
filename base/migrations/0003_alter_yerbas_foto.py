# Generated by Django 5.0.3 on 2024-06-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_customer_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yerbas',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]