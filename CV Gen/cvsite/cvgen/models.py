from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    about = models.TextField()
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    previous_work = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.name
