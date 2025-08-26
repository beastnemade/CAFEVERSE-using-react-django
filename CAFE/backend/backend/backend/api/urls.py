from django.urls import path, include
from . import views

urlpatterns = [
    path('menu/',views.MenuView.as_view()),
    path('order/',views.OrderView.as_view()),
    path('dashboard/<int:pk>/',views.OrderDetailsView.as_view()),
    path('dashboard/',views.OrderView.as_view()),
    path('items/<int:pk>/',views.ItemDetailsView.as_view()),
]