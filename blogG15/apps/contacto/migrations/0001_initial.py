# Generated by Django 5.1.1 on 2024-10-08 00:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
