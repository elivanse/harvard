# Generated by Django 4.1.dev20211210161305 on 2022-02-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0099_remove_listing_image_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('wines', 'Wines'), ('furniture', 'Furniture'), ('clocks', 'Clocks'), ('phones', 'Phones'), ('painting', 'Paintings')], max_length=67),
        ),
    ]
