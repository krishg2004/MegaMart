# Generated by Django 4.2.1 on 2023-05-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default='2021-03-03'),
        ),
    ]
