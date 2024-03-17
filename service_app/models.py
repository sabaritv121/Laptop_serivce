from django.contrib.auth.models import AbstractUser
from django.db import models

#

class Login_view(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)




class Customer(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=50)
    phone_number=models.CharField(max_length=100)
    email = models.EmailField()
    status1=models.BooleanField(default=0)

    def __str__(self):
        return self.name



class Seles_Rentals(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(max_length=50)
    Pancard_number = models.CharField(max_length=16)
    phone_number=models.CharField(max_length=100)
    email = models.EmailField()
    status2 = models.BooleanField(default=0)


class AppointmentSchedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()



class Appointment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(AppointmentSchedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
