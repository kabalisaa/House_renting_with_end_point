# Generated by Django 4.1.7 on 2023-04-03 09:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("renting", "0002_alter_cell_sector"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cell",
            name="cell_name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Cell Name"
            ),
        ),
        migrations.AlterField(
            model_name="district",
            name="district_name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="District Name"
            ),
        ),
        migrations.AlterField(
            model_name="landlord",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                region=None,
                unique=True,
                verbose_name="Phone Number",
            ),
        ),
        migrations.AlterField(
            model_name="manager",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                region=None,
                unique=True,
                verbose_name="Phone Number",
            ),
        ),
        migrations.AlterField(
            model_name="province",
            name="province_name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Province Name"
            ),
        ),
        migrations.AlterField(
            model_name="sector",
            name="sector_name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Sector Name"
            ),
        ),
    ]
