from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, StatsViewSet, PackageBookingviewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename="bookings")
router.register(r'stats', StatsViewSet, basename="stats")
router.register(r'book-package', PackageBookingviewSet, basename="book-package")

urlpatterns = [
    path('', include(router.urls)),
]