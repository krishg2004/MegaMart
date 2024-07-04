# Generated by Django 4.2.1 on 2023-05-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_desc_remove_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
