# Generated by Django 4.2.7 on 2023-11-14 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('productId', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('store', models.CharField(max_length=20, verbose_name='Almacen')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('category', models.CharField(max_length=100, verbose_name='Categoria')),
                ('make', models.CharField(max_length=20, verbose_name='marca')),
                ('describe', models.CharField(max_length=100, null=True, verbose_name='Descripción')),
                ('basicNeed', models.BooleanField(max_length=1, null=True, verbose_name='Nececidad Basica')),
            ],
            options={
                'verbose_name': 'Productos',
                'verbose_name_plural': 'Productos',
                'unique_together': {('productId', 'store')},
            },
        ),
    ]
