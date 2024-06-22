from django.contrib import admin
from .models import RoomType, Hotel, HotelImage

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'website', 'number_of_rooms')
    search_fields = ('name', 'address', 'email', 'room_type')
    inlines = [HotelImageInline]
    
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImage)
admin.site.register(RoomType, RoomTypeAdmin)

