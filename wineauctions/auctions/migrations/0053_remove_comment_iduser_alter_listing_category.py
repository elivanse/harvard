# Generated by Django 4.1.dev20211210161305 on 2022-01-28 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0052_alter_listing_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='idUser',
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('sh', 'Shiraz'), ('mc', 'Malbec'), ('sb', 'Sauvignon Blanc'), ('mt', 'Merlot'), ('pb', 'Pinot Blanc'), ('pn', 'Pinot Noir'), ('cd', 'Chardonnay'), ('cf', 'Cabernet Franc'), ('cs', 'Cabernet Sauvignon'), ('sy', 'Syrah')], max_length=67),
        ),
    ]