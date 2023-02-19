from django.db import models

# Create your models here.
from django.db import models


class Passenger(models.Model):
  
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class Owner(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    insuarance_number = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    number_plate  = models.CharField(max_length=8, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.number_plate

    class Meta:
        ordering = ["number_plate",]


class Voyague(models.Model):
    
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.departure_time

    class Meta:
        ordering = ["departure_time"]

class PaymentStatus(models.Model):
    STATUS_PAID = 'paid'
    STATUS_NOT_PAID = 'notpaid'

    STATUS_CHOICES = [
        (STATUS_PAID, 'paid'),
        (STATUS_NOT_PAID, 'notpaid'),
    ]

    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, default=STATUS_NOT_PAID)

    

class Bookings(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_COMPLETE = 'deliverd'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'pending'),
        (STATUS_COMPLETE, 'deliverd'),
    ]
    
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    voyague  = models.ForeignKey(Voyague, on_delete=models.CASCADE)
    seat_number  = models.IntegerField()
    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, default=STATUS_PENDING)
    

    # def __str__(self) -> str:
    #     return self.passenger

    class Meta:
        ordering = ["passenger"]


class Payments(models.Model):
    voyague = models.ForeignKey(Voyague, on_delete=models.CASCADE)
    amount = models.IntegerField()
    # passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    status = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Bookings, on_delete=models.CASCADE)