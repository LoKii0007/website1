# Generated by Django 4.2.2 on 2023-07-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_example'),
    ]

    operations = [
        migrations.CreateModel(
            name='example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]