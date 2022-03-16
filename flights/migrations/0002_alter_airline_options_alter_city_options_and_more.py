# Generated by Django 4.0 on 2021-12-08 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="airline",
            options={
                "verbose_name": "Авиакомпания",
                "verbose_name_plural": "Авиакомпании",
            },
        ),
        migrations.AlterModelOptions(
            name="city",
            options={"verbose_name": "Город", "verbose_name_plural": "Города"},
        ),
        migrations.AlterModelOptions(
            name="country",
            options={"verbose_name": "Страна", "verbose_name_plural": "Страны"},
        ),
        migrations.AlterModelOptions(
            name="flight",
            options={"verbose_name": "Рейс", "verbose_name_plural": "Рейсы"},
        ),
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "Заказ", "verbose_name_plural": "Заказы"},
        ),
        migrations.AlterModelOptions(
            name="passangerbio",
            options={
                "verbose_name": "Информация о пассажире",
                "verbose_name_plural": "Аинформация о пассажире",
            },
        ),
        migrations.AlterModelOptions(
            name="seat",
            options={"verbose_name": "Место", "verbose_name_plural": "Места"},
        ),
        migrations.AlterField(
            model_name="airline",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="city",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cities",
                to="flights.country",
                verbose_name="Страна",
            ),
        ),
        migrations.AlterField(
            model_name="city",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="country",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="flight",
            name="airline",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="flights",
                to="flights.airline",
                verbose_name="Авиакомпания",
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="departure_city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departure_flights",
                to="flights.city",
                verbose_name="Город вылета",
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="departure_date",
            field=models.DateTimeField(verbose_name="Дата и время вылета"),
        ),
        migrations.AlterField(
            model_name="flight",
            name="flight_class",
            field=models.PositiveIntegerField(
                choices=[(1, "Первый класс"), (2, "Бизнес-класс"), (3, "Эконом-класс")],
                default=3,
                verbose_name="Класс",
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="landing_city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="landing_flights",
                to="flights.city",
                verbose_name="Город посадки",
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="landing_date",
            field=models.DateTimeField(verbose_name="Дата и время посадки"),
        ),
        migrations.AlterField(
            model_name="flight",
            name="price_per_seat",
            field=models.FloatField(verbose_name="Цена за место"),
        ),
        migrations.AlterField(
            model_name="order",
            name="contact_face",
            field=models.CharField(max_length=100, verbose_name="Контактное лицо"),
        ),
        migrations.AlterField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата и время создания"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Электронная почта"),
        ),
        migrations.AlterField(
            model_name="order",
            name="phonenumber",
            field=models.CharField(max_length=30, verbose_name="Номер телефона"),
        ),
        migrations.AlterField(
            model_name="order",
            name="seat",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order",
                to="flights.seat",
                verbose_name="Место",
            ),
        ),
        migrations.AlterField(
            model_name="passangerbio",
            name="citizenship_country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="passangers",
                to="flights.country",
                verbose_name="Страна гражданства",
            ),
        ),
        migrations.AlterField(
            model_name="passangerbio",
            name="date_of_birth",
            field=models.DateField(verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="passangerbio",
            name="document",
            field=models.CharField(max_length=100, verbose_name="Документ"),
        ),
        migrations.AlterField(
            model_name="passangerbio",
            name="document_id",
            field=models.CharField(max_length=100, verbose_name="Номер документа"),
        ),
        migrations.AlterField(
            model_name="passangerbio",
            name="first_name",
            field=models.CharField(max_length=100, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="passangerbio",
            name="gender",
            field=models.IntegerField(
                choices=[(1, "Мужской"), (2, "Женский"), (3, "Неизвестно")],
                default=3,
                verbose_name="Пол",
            ),
        ),
        migrations.AlterField(
            model_name="passangerbio",
            name="last_name",
            field=models.CharField(max_length=100, verbose_name="Фамилия"),
        ),
        migrations.AlterField(
            model_name="passangerbio",
            name="order",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="passanger_bio",
                to="flights.order",
                verbose_name="Заказ",
            ),
        ),
        migrations.AlterField(
            model_name="passangerbio",
            name="patronymic",
            field=models.CharField(max_length=100, verbose_name="Отчество"),
        ),
        migrations.AlterField(
            model_name="seat",
            name="flight",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="seats",
                to="flights.flight",
                verbose_name="Рейс",
            ),
        ),
        migrations.AlterField(
            model_name="seat",
            name="number",
            field=models.CharField(max_length=100, verbose_name="Номер"),
        ),
    ]
