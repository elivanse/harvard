# Generated by Django 4.1.dev20211210161305 on 2022-02-05 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0070_remove_watchlist_title_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('sy', 'Syrah'), ('cs', 'Cabernet Sauvignon'), ('mc', 'Malbec'), ('mt', 'Merlot'), ('sh', 'Shiraz'), ('pb', 'Pinot Blanc'), ('sb', 'Sauvignon Blanc'), ('cf', 'Cabernet Franc'), ('pn', 'Pinot Noir'), ('cd', 'Chardonnay')], max_length=67),
        ),
    ]