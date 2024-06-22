from django.shortcuts import render
from .models import RoomType, Hotel, HotelImage
from .serializers import RoomTypeSerializer, HotelSerializer, HotelImageSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
             
         
    

