# Generated by Django 2.2 on 2021-06-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_auto_20210605_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
