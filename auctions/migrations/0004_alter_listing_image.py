# Generated by Django 4.0.6 on 2022-08-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_user_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]