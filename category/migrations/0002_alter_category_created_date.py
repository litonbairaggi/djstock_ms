# Generated by Django 4.1 on 2022-09-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
