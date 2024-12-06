# Generated by Django 5.1.4 on 2024-12-06 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('tematica', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('horario', models.TimeField()),
                ('lugar', models.CharField(max_length=200)),
            ],
        ),
    ]