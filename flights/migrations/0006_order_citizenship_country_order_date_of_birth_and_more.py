# Generated by Django 4.0 on 2021-12-14 14:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_seat_is_bought'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='citizenship_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passangers', to='flights.country', verbose_name='Страна гражданства'),
        ),
        migrations.AddField(
            model_name='order',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2021, 12, 14), verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='order',
            name='document',
            field=models.CharField(default='', max_length=100, verbose_name='Документ'),
        ),
        migrations.AddField(
            model_name='order',
            name='document_id',
            field=models.CharField(default='', max_length=100, verbose_name='Номер документа'),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='', max_length=100, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='order',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Мужской'), (2, 'Женский'), (3, 'Неизвестно')], default=3, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='', max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='order',
            name='patronymic',
            field=models.CharField(default='', max_length=100, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Итоговая Цена'),
        ),
        migrations.DeleteModel(
            name='PassangerBIO',
        ),
    ]