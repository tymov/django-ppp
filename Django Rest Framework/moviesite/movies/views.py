from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre="Action")
    serializer_class = MovieSerializer
    
class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre="Thriller")
    serializer_class = MovieSerializer
    
class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre="Science Fiction")
    serializer_class = MovieSerializer