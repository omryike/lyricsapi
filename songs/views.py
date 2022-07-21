from django.shortcuts import render
from rest_framework import viewsets
from .models import Song,Artist
from .serializers import SongSerializer,ArtistSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ArtistView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['artist']