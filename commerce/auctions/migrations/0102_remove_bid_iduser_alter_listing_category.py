# Generated by Django 4.1.dev20211210161305 on 2022-02-11 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0101_bid_iduser_alter_listing_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='idUser',
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('phones', 'Phones'), ('clocks', 'Clocks'), ('wines', 'Wines'), ('painting', 'Paintings'), ('furniture', 'Furniture')], max_length=67),
        ),
    ]
