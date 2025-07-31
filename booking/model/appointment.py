from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=20)
    time = models.DateTimeField()
    status = models.CharField(max_length=20, default='Booked')
    address = models.CharField(max_length=20, default=None)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
