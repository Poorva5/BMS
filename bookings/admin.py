from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'user', 'check_in_date', 'check_out_date', 'number_of_guests', 'cost')
    search_fields = ('hotel__name', 'user__username')
    ordering = ('created_at',)

admin.site.register(Booking, BookingAdmin)
