from rest_framework import serializers
from .models import Package, PackageImage, PackageReview
from hotels.models import Hotel
from hotels.serializers import HotelSerializer


class PackageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageImage
        fields = ['id', 'image']


class PackageReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageReview
        fields = ['id', 'user', 'review', 'rating']


class PackageSerializer(serializers.ModelSerializer):
    images = PackageImageSerializer(many=True, required=False)
    reviews = PackageReviewSerializer(many=True, read_only=True)
    hotels = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())

    class Meta:
        model = Package
        fields = ['id', 'name', 'title','description', 'cost', 'hotels', 'images', 'reviews', 'total_bookings', 'duration']
        
        
    def create(self, validated_data):
        hotel = validated_data.pop('hotels')
        package = Package.objects.create(hotels=hotel, **validated_data)
        return package
    
    
    def update(self, instance, validated_data):
        hotel = validated_data.pop('hotels', None)
        if hotel is not None:
            instance.hotel = hotel
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance