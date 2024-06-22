from django.contrib import admin
from .models import UserData
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    ordering = ('username',)

admin.site.register(UserData, CustomUserAdmin)