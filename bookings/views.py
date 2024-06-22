from django.shortcuts import render
from .models import Booking, PackageBooking
from .serializers import BookingSerializer, PackageBookingSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.utils.timezone import now, timedelta
from hotels.models import Hotel
from rest_framework.response import Response


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class PackageBookingviewSet(viewsets.ModelViewSet):
    queryset = PackageBooking.objects.all()
    serializer_class = PackageBookingSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    
        

class StatsViewSet(viewsets.ModelViewSet):
    
    def list(self, request):
        User = get_user_model()
        
        # New bookings under 2 days
        two_days_ago = now() - timedelta(days=2)
        new_bookings = Booking.objects.filter(created_at__gte=two_days_ago).count()
        
        # Total number of users excluding is_staff and is_superuser
        total_users = User.objects.filter(is_staff=False, is_superuser=False).count()
        
        # Total number of employees
        total_employees = User.objects.filter(is_staff=True, is_superuser=True).count()
        
        # Total number of hotels
        total_hotels = Hotel.objects.count()
        
        data = {
            'new_bookings_under_2_days': new_bookings,
            'total_users': total_users,
            'total_employees': total_employees,
            'total_hotels': total_hotels,
        }
        
        return Response(data)
        
        