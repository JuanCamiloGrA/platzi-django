# Generated by Django 5.0.6 on 2024-07-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('description', models.TextField(max_length=255, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('available', models.BooleanField(default=True, verbose_name='Disponible')),
                ('image', models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='Imagen')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
