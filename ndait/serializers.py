from rest_framework import serializers
from ndait.models import (  Passenger, Driver,Owner,  Vehicle, Voyague, PaymentStatus, Payments , Bookings)


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'phone']
    # id = serializers.IntegerField(read_only=True)


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'name', 'phone']
       

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ['id', 'passenger', 'voyague', 'seat_number', "status"]


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'phone']
        



class VehicleSerializer(serializers.ModelSerializer):
    # Driver = serializers.HyperlinkedRelatedField(
    #     queryset=Driver.objects.all(),
    #     view_name='Driver-detail'
    # )

    # recording_officer = serializers.HyperlinkedRelatedField(
    #     queryset=Driver.objects.all(),
    #     view_name='Driver-detail'
    # )

    
    # owner = OwnerSerializer()

    class Meta:
        model = Vehicle
        fields = ['id', 'capacity', 'number_plate' 'owner', 'insuarance_number']
        



class VoyagueSerializer(serializers.ModelSerializer):
    # vehicle = VehicleSerializer(many=True)
    # driver = DriverSerializer(many=True)


    class Meta:
        model = Voyague
        fields = ['vehicle', 'driver', 'origin',
                  'destination', 'departure_time']
    # vehicle = serializers.CharField(read_only=True)
    # driver = serializers.CharField(read_only=True)


class PaymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentStatus
        fields = ['id', 'status']


class PaymentSerializer(serializers.ModelSerializer):
   
    # voyague = VoyagueSerializer(many=True)
    # passenger = PassengerSerializer(many=True)

    class Meta:
        model = Payments
        fields = ['id', 'voyague', 'amount', 'status']

