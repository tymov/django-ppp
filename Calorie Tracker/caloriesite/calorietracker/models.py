from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=100)
    energy = models.FloatField(default=0)  # Provide a default value
    protein = models.FloatField(default=0)  # Provide a default value
    fat = models.FloatField(default=0)  # Provide a default value
    saturated_fat = models.FloatField(default=0)  # Provide a default value
    carbohydrate = models.FloatField(default=0)  # Provide a default value
    sugars = models.FloatField(default=0)  # Provide a default value
    dietary_fibre = models.FloatField(default=0)  # Provide a default value
    sodium = models.FloatField(default=0)  # Provide a default value
    calories = models.FloatField(default=0)  # Provide a default value
    tags = models.JSONField(default=list)  # Provide a default value

    def __str__(self):
        return self.name

class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)