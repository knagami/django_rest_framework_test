from rest_framework import routers
from .views import UserViewSet, EntryViewSet, ImageViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'images', ImageViewSet)