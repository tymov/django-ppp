from django.db import models

# Create your models here.
class Link(models.Model):
    address = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name