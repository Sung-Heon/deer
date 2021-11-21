from django.urls import path

from .views import CalculateChargeView

urlpatterns = [
    path('calculate-charge', CalculateChargeView.as_view()),
]