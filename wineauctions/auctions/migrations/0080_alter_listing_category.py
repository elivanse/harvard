# Generated by Django 4.1.dev20211210161305 on 2022-02-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0079_alter_listing_category_alter_listing_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('sh', 'Shiraz'), ('pb', 'Pinot Blanc'), ('mc', 'Malbec'), ('sb', 'Sauvignon Blanc'), ('pn', 'Pinot Noir'), ('sy', 'Syrah'), ('cd', 'Chardonnay'), ('cs', 'Cabernet Sauvignon'), ('mt', 'Merlot'), ('cf', 'Cabernet Franc')], max_length=67),
        ),
    ]
