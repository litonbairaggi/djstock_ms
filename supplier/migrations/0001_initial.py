# Generated by Django 4.0.3 on 2022-07-22 02:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=220)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
