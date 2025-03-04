# Generated by Django 5.0.6 on 2024-06-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='province_or_state',
            field=models.CharField(max_length=50),
        ),
    ]
