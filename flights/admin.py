from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Airline, Country, City, Flight, Order, Seat

admin.site.unregister(Group)


class SeatInline(admin.StackedInline):
    model = Seat
    fields = ["number"]
    extra = 1


class AirlineAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    fields = ["id", "name"]
    readonly_fields = ["id"]


class CountryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    fields = ["id", "name"]
    readonly_fields = ["id"]


class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "country"]
    fields = ["id", "name", "country"]
    readonly_fields = ["id"]


class FlightAdmin(admin.ModelAdmin):
    list_display = ["id", "airline", "departure_city", "landing_city", "price_per_seat"]
    fields = [
        "id",
        "airline",
        "departure_city",
        "departure_date",
        "landing_city",
        "landing_date",
        "price_per_seat",
        "price_per_seat_underage",
        "flight_class",
    ]
    readonly_fields = ["id"]
    inlines = [SeatInline]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "seat", "flight_name"]
    fields = [
        "id",
        "seat",
        "flight_name",
        "email",
        "phonenumber",
        "contact_face",
        "created_at",
        "first_name",
        "last_name",
        "patronymic",
        "gender",
        "date_of_birth",
        "citizenship_country",
        "document",
        "document_id",
        "total_price",
        "is_active"
    ]
    readonly_fields = ["id", "created_at", "flight_name"]


admin.site.register(Airline, AirlineAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Order, OrderAdmin)
