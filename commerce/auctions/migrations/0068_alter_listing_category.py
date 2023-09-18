# Generated by Django 4.1.dev20211210161305 on 2022-01-29 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0067_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('sb', 'Sauvignon Blanc'), ('pb', 'Pinot Blanc'), ('mt', 'Merlot'), ('pn', 'Pinot Noir'), ('sy', 'Syrah'), ('cs', 'Cabernet Sauvignon'), ('sh', 'Shiraz'), ('cf', 'Cabernet Franc'), ('cd', 'Chardonnay'), ('mc', 'Malbec')], max_length=67),
        ),
    ]