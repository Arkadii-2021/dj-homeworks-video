from rest_framework import serializers
from .models import Sensor, Measurement


class AdvancedMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'picture']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id',  'name', 'description']


class MeasurementSerializer(serializers.Serializer):
    sensor_id = serializers.IntegerField()
    temperature = serializers.FloatField()
    picture = serializers.ImageField(required=False)
    created_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = AdvancedMeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

