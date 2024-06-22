from django.contrib import admin
from .models import Package, PackageImage, PackageReview

class PackageImageInline(admin.TabularInline):
    model = PackageImage
    extra = 1


class PackageReviewInline(admin.TabularInline):
    model = PackageReview
    extra = 1


class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'cost')
    search_fields = ('name',)
    inlines = [PackageImageInline, PackageReviewInline]


admin.site.register(Package, PackageAdmin)
admin.site.register(PackageImage)
admin.site.register(PackageReview)