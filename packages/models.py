from django.db import models
from django.conf import settings
from hotels.models import Hotel
from utils.models import BaseModel


class Package(BaseModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    hotels = models.ForeignKey(Hotel, related_name='packages', on_delete=models.CASCADE, null=True, blank=True)
    total_bookings = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    

class PackageImage(BaseModel):
    package = models.ForeignKey(Package, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='packages/images/')

    def __str__(self):
        return f"Image for {self.package.name}"
    
    
class PackageReview(BaseModel):
    package = models.ForeignKey(Package, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.package.name}"