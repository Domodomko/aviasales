from django.urls import path

from .views import FlightsListView, FlightDetailView, SeatPurchaseView, OrderSuccessView, OrderReturnView, OrdersListView


urlpatterns = [
    path("", FlightsListView.as_view(), name="flights-list"),
    path("flight/<int:pk>", FlightDetailView.as_view(), name="flight-detail"),
    path("seat-purchase", SeatPurchaseView.as_view(), name="seat-purchase"),
    path("order-success", OrderSuccessView.as_view(), name="order-success"),
    path("order-return", OrderReturnView.as_view(), name="order-return"),
    path("orders", OrdersListView.as_view(), name="orders-list"),
]
