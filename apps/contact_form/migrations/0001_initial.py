# Generated by Django 5.0.6 on 2024-06-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('form_class', models.CharField(choices=[('Sugerencia', 'Suggest'), ('Duda', 'Query'), ('Petición', 'Claim'), ('Opinion', 'Opinion')], max_length=30)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Contact_form',
                'verbose_name_plural': 'Contact-forms',
            },
        ),
    ]
