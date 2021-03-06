# Generated by Django 4.0 on 2021-12-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0002_alter_airline_options_alter_city_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="flight",
            name="price_per_seat_infant",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Цена за десткое место (в долларах)"
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="price_per_seat",
            field=models.FloatField(verbose_name="Цена за место (в долларах)"),
        ),
    ]
