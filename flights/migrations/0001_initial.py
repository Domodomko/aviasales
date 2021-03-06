# Generated by Django 4.0 on 2021-12-08 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airline",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("departure_date", models.DateTimeField()),
                ("landing_date", models.DateTimeField()),
                ("flight_class", models.PositiveIntegerField()),
                ("price_per_seat", models.FloatField()),
                (
                    "airline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flights",
                        to="flights.airline",
                    ),
                ),
                (
                    "departure_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departure_flights",
                        to="flights.city",
                    ),
                ),
                (
                    "landing_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="landing_flights",
                        to="flights.city",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("phonenumber", models.CharField(max_length=30)),
                ("contact_face", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Seat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=100)),
                (
                    "flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seats",
                        to="flights.flight",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PassangerBIO",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("patronymic", models.CharField(max_length=100)),
                ("gender", models.IntegerField()),
                ("date_of_birth", models.DateField()),
                ("document", models.CharField(max_length=100)),
                ("document_id", models.CharField(max_length=100)),
                (
                    "citizenship_country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="passangers",
                        to="flights.country",
                    ),
                ),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="passanger_bio",
                        to="flights.order",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="seat",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order",
                to="flights.seat",
            ),
        ),
        migrations.AddField(
            model_name="city",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cities",
                to="flights.country",
            ),
        ),
    ]
