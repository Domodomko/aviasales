from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from datetime import date

from .constants import GenderConstants, FlightClassConstants


class Flight(models.Model):
    airline = models.ForeignKey(
        "Airline",
        on_delete=models.CASCADE,
        related_name="flights",
        verbose_name="Авиакомпания",
    )
    departure_city = models.ForeignKey(
        "City",
        on_delete=models.CASCADE,
        related_name="departure_flights",
        verbose_name="Город вылета",
    )
    landing_city = models.ForeignKey(
        "City",
        on_delete=models.CASCADE,
        related_name="landing_flights",
        verbose_name="Город посадки",
    )
    departure_date = models.DateTimeField(verbose_name="Дата и время вылета")
    landing_date = models.DateTimeField(verbose_name="Дата и время посадки")
    flight_class = models.PositiveIntegerField(
        choices=FlightClassConstants.CHOICES,
        default=FlightClassConstants.ECONOMY,
        verbose_name="Класс",
    )
    price_per_seat = models.FloatField(verbose_name="Цена за место (в долларах)")
    price_per_seat_underage = models.FloatField(
        verbose_name="Цена за десткое место (в долларах)", blank=True, null=True
    )

    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"

    def clean(self):
        if self.departure_date < self.landing_date:
            raise ValidationError(
                {"departure_date": f"Дата вылета неможет быть позже даты прилёта."})

    def __str__(self):
        return f"{self.airline}: {self.departure_city}-{self.landing_city} #{self.pk}"

    def free_seats(self):
        return self.seats.count()


class Airline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Авиакомпания"
        verbose_name_plural = "Авиакомпании"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    country = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        related_name="cities",
        verbose_name="Страна",
    )

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name


class Seat(models.Model):
    flight = models.ForeignKey(
        "Flight", on_delete=models.CASCADE, related_name="seats", verbose_name="Рейс"
    )
    number = models.CharField(max_length=100, verbose_name="Номер")
    is_bought = models.BooleanField(default=False, verbose_name="Куплено")

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return f"{self.flight}: {self.number}"


class Order(models.Model):
    seat = models.OneToOneField(
        "Seat", on_delete=models.CASCADE, related_name="order", verbose_name="Место"
    )
    email = models.EmailField(verbose_name="Электронная почта")
    phonenumber = models.CharField(max_length=30, verbose_name="Номер телефона")
    contact_face = models.CharField(max_length=100, verbose_name="Контактное лицо")
    created_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата и время создания"
    )

    first_name = models.CharField(max_length=100, verbose_name="Имя", default="")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", default="")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество", default="")
    gender = models.IntegerField(
        choices=GenderConstants.CHOICES,
        default=GenderConstants.UNKNOWN,
        verbose_name="Пол",
    )
    date_of_birth = models.DateField(verbose_name="Дата рождения", default=timezone.now)
    citizenship_country = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        related_name="passangers",
        verbose_name="Страна гражданства",
        null=True,
    )
    document = models.CharField(max_length=100, verbose_name="Документ", default="")
    document_id = models.CharField(max_length=100, verbose_name="Номер документа", default="")
    total_price = models.FloatField(verbose_name="Итоговая Цена", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Актуален")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ #{self.pk}"
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.seat.flight.departure_date < timezone.now():
            raise ValidationError(
                {"email": f"Рейс уже неактуален."})

        super().save(force_insert, force_update, *args, **kwargs)

    def flight_name(self):
        return self.seat.flight

    flight_name.short_description = "Рейс"
