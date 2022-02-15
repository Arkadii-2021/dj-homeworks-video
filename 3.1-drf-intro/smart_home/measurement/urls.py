from django.contrib import admin
from django.urls import path

from measurement.views import SensorView, MeasurementView, SensorsDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorsDetailView.as_view()),
    path("measurements/", MeasurementView.as_view()),
]
