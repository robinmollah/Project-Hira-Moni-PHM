# Generated by Django 3.0.7 on 2020-06-17 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_remove_details_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='crime_count',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]