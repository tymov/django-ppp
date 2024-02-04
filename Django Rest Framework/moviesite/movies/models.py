from django.db import models

# Create your models here.
class Moviedata(models.Model):
    
    def __str__ (self):
        return self.name
    
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)
    rating = models.FloatField()
    genre = models.CharField(max_length=100, default="No genre")
    image = models.ImageField(upload_to="movies/images", default="movies/images/default.jpg")
    