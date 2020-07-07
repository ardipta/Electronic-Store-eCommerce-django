# Generated by Django 2.2.10 on 2020-07-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobilephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=250, unique=True)),
                ('brand_name', models.CharField(max_length=250)),
                ('old_price', models.CharField(max_length=250)),
                ('new_price', models.CharField(max_length=250)),
                ('specification', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=150, verbose_name='Description')),
                ('image_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('image_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-list_date',),
            },
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=250, unique=True)),
                ('brand_name', models.CharField(max_length=250)),
                ('old_price', models.CharField(max_length=250)),
                ('new_price', models.CharField(max_length=250)),
                ('ram', models.CharField(max_length=250)),
                ('specification', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=150, verbose_name='Description')),
                ('image_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('image_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-list_date',),
            },
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=250, unique=True)),
                ('brand_name', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
                ('specification', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=150, verbose_name='Description')),
                ('image_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('image_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-list_date',),
            },
        ),
    ]
