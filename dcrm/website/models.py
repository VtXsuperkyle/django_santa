from django.db import models
from django.contrib.auth.models import AbstractUser

class santa_user(AbstractUser): #make changes in settings when you do this
    points = models.IntegerField(default=0)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    city = models.CharField(max_length=50, blank=True)

class reindeerbooking(models.Model):
    booking_id = models.AutoField(primary_key=True, editable=False)
    ride_user_id = models.ForeignKey(santa_user, on_delete=models.CASCADE)
    ride_booking_date = models.DateField(auto_now_add=True)
    ride_booking_date_arrive = models.DateField()
    ride_booking_date_leave = models.DateField()
    ride_booking_adults = models.IntegerField(default=0)
    ride_booking_children = models.IntegerField(default=0)
    ride_total_cost = models.FloatField(default=0)

















