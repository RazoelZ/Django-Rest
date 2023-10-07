from django.urls import path
from .views import CarsViewSet

urlpatterns = [
    path('cars/', CarsViewSet.as_view()),
    path('cars/<int:id>/', CarsViewSet.as_view()),
]
