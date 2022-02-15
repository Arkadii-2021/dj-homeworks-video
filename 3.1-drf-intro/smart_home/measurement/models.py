from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, primary_key=True, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    picture = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now=True)

