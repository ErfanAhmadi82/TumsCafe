# Generated by Django 4.2.2 on 2023-08-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_cartitem_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order Recived', 'Order Recived'), ('Getting Yor Order Ready', 'Getting Yor Order Ready'), ('Done!', 'Done!')], default='Order Recived', max_length=40),
        ),
    ]