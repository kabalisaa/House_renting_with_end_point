# Generated by Django 4.1.7 on 2023-03-31 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='renting.sector', verbose_name='Sector'),
        ),
    ]
