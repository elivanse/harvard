# Generated by Django 3.2.6 on 2021-09-20 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20210920_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_lst',
            name='category',
            field=models.CharField(choices=[('fish', 'Fishing goods'), ('all', 'All categories'), ('shoe', 'Shoes'), ('nt', 'Notebooks'), ('ant', 'Antiquities'), ('dt', 'Desktop Computer')], default={('fish', 'Fishing goods'), ('all', 'All categories'), ('shoe', 'Shoes'), ('nt', 'Notebooks'), ('ant', 'Antiquities'), ('dt', 'Desktop Computer')}, max_length=67),
        ),
    ]