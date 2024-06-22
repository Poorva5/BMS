from django.shortcuts import render
from .models import Package, PackageReview, PackageImage
from .serializers import PackageSerializer, PackageReviewSerializer
from rest_framework import viewsets

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    def perform_create(self, serializer):
        serializer.save()
        
    def perform_update(self, serializer):
        serializer.save()


class PackageReviewViewSet(viewsets.ModelViewSet):
    queryset = PackageReview.objects.all()
    serializer_class = PackageReviewSerializer
    