# Generated by Django 4.2.2 on 2023-07-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_products_producttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField()),
                ('image', models.ImageField(upload_to='home/images')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=5000)),
                ('sub_description', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]