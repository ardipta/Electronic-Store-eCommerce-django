# Generated by Django 2.2.10 on 2020-07-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilephone',
            name='specification',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='specification',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='specification',
            field=models.TextField(max_length=500),
        ),
    ]