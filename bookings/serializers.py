from rest_framework import serializers
from .models import Booking, PackageBooking
from hotels.serializers import RoomTypeSerializer, HotelSerializer
from packages.serializers import PackageSerializer


class BookingSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer(read_only=True)
    hotel = HotelSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'id', 'hotel', 'user', 'room_type', 'check_in_date', 
            'check_out_date', 'number_of_guests', 'cost'
        ]
    
    
class StatsSerializer(serializers.Serializer):
    new_bookings_under_2_days = serializers.IntegerField()
    total_users = serializers.IntegerField()
    total_employees = serializers.IntegerField()
    total_hotels = serializers.IntegerField()
    
    
class PackageBookingSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    hotel = HotelSerializer(source='package.hotels', read_only=True)
    package = PackageSerializer(source='packages', read_only=True, many=True)
    
    class Meta:
        model = PackageBooking
        fields = ['id', 'user', 'package','hotel', 'booking_date', 'number_of_guests', 'status', 'total_cost']
        
    def get_total_cost(self, obj):
        return obj.calculate_total_cost()