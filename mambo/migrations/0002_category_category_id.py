# Generated by Django 4.2.5 on 2023-09-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mambo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
