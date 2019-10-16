from django.shortcuts import render

# Create your views here.
import django_filters
from rest_framework import viewsets, filters
import os
from rest_framework.response import Response
from .models import User, Entry, Image
from .serializer import UserSerializer, EntrySerializer, ImageSerializer
from django.conf import settings
UPLOAD_DIR = 'static/uploaded/'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ('author', 'status')
    
    
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request):
        file = request.FILES['file']
        path = os.path.join(settings.MEDIA_NAME + '/', file.name)
        destination = open(path, 'wb')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()

        if not os.path.exists(path):
            print('File not found:', path)
            return create_render(request)

        image, created = Image.objects.get_or_create(filepath=path)
        if created:
            # image.sender = request.POST['sender']
            image.created_at = request.POST['created_at']
            image.updated_at = request.POST['updated_at']
            image.save()

        return Response({'message': 'OK'})