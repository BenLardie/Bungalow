# Generated by Django 2.2.6 on 2019-10-08 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bungalow_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='area_unit',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='bathrooms',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='bedrooms',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='home_size',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='home_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='last_sold_date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='last_sold_price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='property_size',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='rent_price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='rentzestimate_amount',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='rentzestimate_last_updated',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='state',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='tax_value',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='tax_year',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='year_built',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='zestimate_amount',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='zestimate_last_updated',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='zillow_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='zipcode',
            field=models.CharField(max_length=255),
        ),
    ]
