from django.db import models

# Create your models here.
class Expense(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100)
    