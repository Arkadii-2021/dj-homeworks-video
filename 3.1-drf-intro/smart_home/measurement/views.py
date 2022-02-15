from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorsDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
