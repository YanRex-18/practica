# Generated by Django 5.1.3 on 2024-11-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre del producto')),
                ('description', models.TextField(verbose_name='Descripción del producto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio del producto')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
        ),
    ]
