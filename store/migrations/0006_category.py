# Generated by Django 5.0.6 on 2024-05-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_image_productimage_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=20, verbose_name='Category name')),
                ('products', models.ManyToManyField(to='store.product')),
            ],
        ),
    ]
