# Generated by Django 4.0.2 on 2022-02-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0089_alter_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('wines', 'Wines'), ('clocks', 'Clocks'), ('phones', 'Phones'), ('painting', 'Paintings'), ('furniture', 'Furniture')], max_length=67),
        ),
    ]
