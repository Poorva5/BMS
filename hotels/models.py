from django.db import models
from utils.models import BaseModel


class Hotel(BaseModel):
    SINGLE = 'Single'
    DOUBLE = 'Double'
    SUITE = 'Suite'
    FAMILY = 'Family'
    ROOM_TYPES_CHOICES = [
        (SINGLE, 'Single Room'),
        (DOUBLE, 'Double Room'),
        (SUITE, 'Suite'),
        (FAMILY, 'Family Room'),
    ]
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    number_of_rooms = models.IntegerField(null=True, blank=True)
    room_types = models.CharField(max_length=20, choices=ROOM_TYPES_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotels/images/')

    def __str__(self):
        return f"Image for {self.hotel}"