# Generated by Django 4.1.3 on 2023-02-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('economia', '0018_indicadorambiental_subindice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicadorinstitucional',
            name='subindice',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
