# Generated by Django 4.2.2 on 2023-06-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_inquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(default='0123456789')),
                ('description', models.CharField(max_length=500, null='true')),
            ],
        ),
    ]