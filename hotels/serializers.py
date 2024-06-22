from rest_framework import serializers
from .models import RoomType, Hotel, HotelImage
from rest_framework import serializers

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'name']
        
        
class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['id', 'hotel', 'image']
        
        
class HotelSerializer(serializers.ModelSerializer):
    room_types = RoomTypeSerializer(many=True)
    images = HotelImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = [
            'id', 'name', 'address', 'phone', 'email', 'website', 
            'description', 'number_of_rooms', 'room_types', 'images'
        ]
    
    def create(self, validated_data):
        room_types_data = validated_data.pop('room_types')
        hotel = Hotel.objects.create(**validated_data)
        for room_type_data in room_types_data:
            room_type, created = RoomType.objects.get_or_create(**room_type_data)
            hotel.room_types.add(room_type)
        return hotel
             