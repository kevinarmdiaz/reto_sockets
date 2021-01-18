from django.db import models

# Create your models here.
class Device(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=240)
    last_temperature = models.FloatField()
    keep_alive = models.DateTimeField()
    threshold_temperature = models.FloatField()

    def __str__(self):
        return self.name

class AlertDevice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    device = models.ForeignKey(Device,
                                 on_delete=models.CASCADE,
                                 related_name="alerts")