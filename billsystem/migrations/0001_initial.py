# Generated by Django 3.1.3 on 2021-02-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sales_unit', models.CharField(choices=[('KG', 'kg'), ('MG', 'mg'), ('PIECES', 'pieces')], max_length=10)),
                ('in_stock', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('is_available', models.BooleanField(default=False)),
            ],
        ),
    ]
