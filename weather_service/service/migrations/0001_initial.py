# Generated by Django 3.2.8 on 2021-10-13 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Города',
                'db_table': 'city',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather', models.CharField(db_column='weather', max_length=150, verbose_name='Погода')),
                ('time', models.DateTimeField(verbose_name='Время запроса')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='service.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Запросы пользователей',
                'db_table': 'UsersRequests',
                'ordering': ['id'],
            },
        ),
    ]
