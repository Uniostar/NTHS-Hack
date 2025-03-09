from django.db import models

# Create your models here.
class SensorData(models.Model):
    degree = models.IntegerField()

    def __str__(self):
        return f"Degrees: {self.degree}"
