from django.db import models
from utils.models import BaseModel
from hotels.models import Hotel, RoomType
from django.conf import settings
from packages.models import Package


class Booking(BaseModel):
    hotel = models.ForeignKey(Hotel, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, null=True, blank=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.hotel.name
    
    
class PackageBooking(BaseModel):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='package_bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    def __str__(self):
        return f"Booking by {self.user.username} for {self.package.name}"
    
    def calculate_total_cost(self):
        return self.package.cost * self.number_of_guests