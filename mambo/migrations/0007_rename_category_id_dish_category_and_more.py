# Generated by Django 4.2.5 on 2023-10-02 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mambo', '0006_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='dish_id',
            new_name='dish',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='table_id',
            new_name='table',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='order_id',
            new_name='order',
        ),
    ]