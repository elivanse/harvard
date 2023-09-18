# Generated by Django 4.1.dev20211210161305 on 2022-02-07 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0074_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('cf', 'Cabernet Franc'), ('cs', 'Cabernet Sauvignon'), ('mc', 'Malbec'), ('cd', 'Chardonnay'), ('mt', 'Merlot'), ('pb', 'Pinot Blanc'), ('sh', 'Shiraz'), ('pn', 'Pinot Noir'), ('sy', 'Syrah'), ('sb', 'Sauvignon Blanc')], max_length=67),
        ),
    ]