# Generated by Django 2.0.2 on 2018-02-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.IntegerField(max_length=4, primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=10)),
                ('shares', models.IntegerField(max_length=10)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('purchase_date', models.CharField(max_length=9)),
            ],
        ),
    ]