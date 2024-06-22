from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PackageViewSet, PackageReviewViewSet

router = DefaultRouter()
router.register(r'packages', PackageViewSet)
router.register(r'review', PackageReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]