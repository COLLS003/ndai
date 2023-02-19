from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import  Passenger, Driver,Owner,  Vehicle, Voyague, PaymentStatus, Payments , Bookings
from .serializers import (
    PassengerSerializer,  DriverSerializer, VehicleSerializer, OwnerSerializer, VoyagueSerializer, PaymentStatusSerializer, PaymentSerializer, BookingsSerializer    )


class PassengerViewSet(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class VoyagueViewSet(ModelViewSet):
    queryset = Voyague.objects.all()
    serializer_class = VoyagueSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class OwnerViewSet(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
     

class BookingsViewSet(ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer




class PaymentViewSet(ModelViewSet):
    queryset = Payments.objects.prefetch_related('voyague', 'passenger').all()

    serializer_class = PaymentSerializer



class PaymentStatusViewSet(ModelViewSet):
    # queryset = Payments.objects.prefetch_related('voyague', 'passenger').all()
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer



