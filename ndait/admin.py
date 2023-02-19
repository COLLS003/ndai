from django.contrib import admin

from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.utils.html import format_html
from django.utils.http import urlencode
from django.urls import reverse
from . import models
# Passenger, Driver,Owner,  Vehicle, Voyague, PaymentStatus, Payments , Bookings

# Register your models here.
@admin.register(models.Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    # list_editable = ['name', 'phone']
    list_filter = ['name']
    list_per_page = 10
    ordering = ['name', 'phone']
    search_fields = ['name__istartswith',
                     'phone__istartswith', ]

@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    # list_editable = ['name', 'phone']
    list_filter = ['name']
    list_per_page = 10
    ordering = ['name', 'phone']
    search_fields = ['name__istartswith',
                     'phone__istartswith', ]


@admin.register(models.Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    # list_editable = ['name', 'phone']
    list_filter = ['name']
    list_per_page = 10
    ordering = ['name', 'phone']
    search_fields = ['name__istartswith',
                     'phone__istartswith', ]



@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'capacity', 'number_plate',  'owner', 'insuarance_number']
    # list_editable = ['name', 'phone']
    list_filter = ['id', 'capacity', 'number_plate',  'owner', 'insuarance_number']
    list_per_page = 10
    ordering = ['id', 'capacity', 'number_plate',  'owner', 'insuarance_number']
    search_fields = ['number_plate__istartswith',
                     'capacity__istartswith', ]


@admin.register(models.Voyague)
class VoyagueAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'driver', 'origin',
                  'destination', 'departure_time']
    # list_editable = ['name', 'phone']
    list_filter = ['vehicle', 'driver', 'origin',
                  'destination', 'departure_time']
    list_per_page = 10
    ordering = ['vehicle', 'driver', 'origin',
                  'destination', 'departure_time']
    search_fields = ['origin__istartswith',
                     'destination__istartswith', ]

@admin.register(models.PaymentStatus)
class PaymentStatusAdmin(admin.ModelAdmin):
    list_display =['id', 'status']
    # list_editable = ['name', 'phone']
    list_filter = ['status']
    list_per_page = 10
    ordering = ['id', 'status']
    search_fields = ['status__istartswith',
                     'id__istartswith', ]


@admin.register(models.Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display =['id', 'voyague', 'amount', 'status']
    # list_editable = ['name', 'phone']
    list_filter = ['id', 'voyague', 'amount', 'status']
    list_per_page = 10
    ordering = ['id', 'voyague', 'amount', 'status']
    search_fields = ['amount__istartswith',
                     'status__istartswith', ]



@admin.register(models.Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'passenger', 'voyague', 'seat_number', "status"]
    # list_editable = ['name', 'phone']
    list_filter = ['id', 'passenger', 'voyague', 'seat_number', "status"]
    list_per_page = 10
    ordering = ['id', 'passenger', 'voyague', 'seat_number', "status"]
    search_fields = ['passenger__istartswith',
                     'voyague__istartswith', ]