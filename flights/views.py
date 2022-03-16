from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, FormView
from django import forms
from django.urls import reverse
from django.db.models import Count, Sum

from datetime import datetime
from datetime import date

from .models import Flight, City, Order, Seat


class FlightsListView(TemplateView):

    template_name = "flights_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flights_list = Flight.objects.all()

        airline = self.request.GET.get("airline")
        if airline:
            flights_list = flights_list.filter(airline=airline)

        departure_date = self.request.GET.get("departure_date")
        if departure_date:
            flights_list = flights_list.filter(departure_date__date=departure_date)

        landing_date = self.request.GET.get("landing_date")
        if landing_date:
            flights_list = flights_list.filter(landing_date__date=landing_date)

        departure_city = self.request.GET.get("departure_city")
        if departure_city:
            flights_list = flights_list.filter(departure_city=departure_city)

        landing_city = self.request.GET.get("landing_city")
        if landing_city:
            flights_list = flights_list.filter(landing_city=landing_city)

        context["flights_list"] = flights_list
        context["cities"] = City.objects.all()

        return context


class FlightDetailView(DetailView):
    model = Flight

    template_name = "flight_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["flight"] = self.object

        return context


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "email",
            "phonenumber",
            "contact_face",
            "first_name",
            "last_name",
            "patronymic",
            "gender",
            "date_of_birth",
            "citizenship_country",
            "document",
            "document_id",
        ]
    
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth > date.today():
            raise forms.ValidationError("Дата рождения не может быть в будущем!")
        return date_of_birth


class SeatPurchaseView(FormView):
    model = Order
    form_class = OrderForm

    template_name = "seat_purchase.html"

    def get_success_url(self):        
        seat = Seat.objects.get(id=self.request.GET.get("seat"))                   
        return reverse('flight-detail', kwargs={'pk' : seat.flight.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            seat = Seat.objects.get(id=self.request.GET.get("seat"), is_bought=False)
            context["seat"] = seat
        except Seat.DoesNotExist:
            context["fail_message"] = "Указанное вами сиденье уже занято или его не сущетсвует."

        return context

    def form_valid(self, form):
        today = date.today()
        age = today.year - form.instance.date_of_birth.year - ((today.month, today.day) < (form.instance.date_of_birth.month, form.instance.date_of_birth.day))
        seat = Seat.objects.get(id=self.request.GET.get("seat"))
        if age < 18:
            form.instance.total_price = seat.flight.price_per_seat_underage
        else:
            form.instance.total_price = seat.flight.price_per_seat

        form.instance.seat = seat
        form.instance.save()
        seat.is_bought = True
        seat.save()
        return super().form_valid(form)


class OrderSuccessView(TemplateView):

    template_name = "order_success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            order = Order.objects.get(pk=self.request.GET.get("order"))
            context["order"] = order
        except Order.DoesNotExist:
            context["fail_message"] = "Указанный вами заказ не существует."

        return context


class OrderReturnView(TemplateView):

    template_name = "order_return.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            order = Order.objects.get(pk=self.request.GET.get("order"), is_active=True)
            seat = order.seat
            seat.is_bought = False
            seat.save()
            order.is_active = False
            order.save()
            context["order"] = order
        except Order.DoesNotExist:
            context["fail_message"] = "Указанного вами билета не существует или он уже возвращён."

        return context



class OrdersListView(TemplateView):

    template_name = "orders_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders_list = Order.objects.all()

        starts_at = self.request.GET.get("starts_at")
        if starts_at:
            orders_list = orders_list.filter(created_at__date__gte=starts_at)

        ends_at = self.request.GET.get("ends_at")
        if ends_at:
            orders_list = orders_list.filter(created_at__date__lte=ends_at)

        context["orders_list"] = orders_list
        orders_list = orders_list.filter(is_active=True).aggregate(total_sum=Sum("total_price"))
        context["orders_sum"] = orders_list.get("total_sum")

        return context