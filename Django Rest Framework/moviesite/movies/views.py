from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# REST API ViewSets
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
    
# HTML Views
def movie_list(request):
    movie_objects = Moviedata.objects.all()
    
    # Search & Filtering
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_objects = movie_objects.filter(name__icontains=movie_name)
        
    # Pagination
    paginator = Paginator(movie_objects, 4)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)
    
    return render(request, 'movies/movies.html', {'movies': movie_objects})