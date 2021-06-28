# Generated by Django 2.2 on 2021-06-06 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_auto_20210606_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=6)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Ingredient')),
            ],
        ),
    ]