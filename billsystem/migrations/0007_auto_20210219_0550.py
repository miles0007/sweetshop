# Generated by Django 3.1.6 on 2021-02-19 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billsystem', '0006_commodity_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]