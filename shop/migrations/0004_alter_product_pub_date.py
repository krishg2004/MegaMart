# Generated by Django 4.2.1 on 2023-05-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category_product_desc_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default='0000-00-00'),
        ),
    ]
