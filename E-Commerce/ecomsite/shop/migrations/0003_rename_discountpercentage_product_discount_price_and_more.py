# Generated by Django 4.2.9 on 2024-02-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discountPercentage',
            new_name='discount_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
