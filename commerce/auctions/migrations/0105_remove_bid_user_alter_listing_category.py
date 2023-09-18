# Generated by Django 4.1.dev20211210161305 on 2022-02-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0104_remove_bid_iduser_bid_user_alter_listing_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('wines', 'Wines'), ('painting', 'Paintings'), ('clocks', 'Clocks'), ('phones', 'Phones'), ('furniture', 'Furniture')], max_length=67),
        ),
    ]