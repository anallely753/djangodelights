from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=50)
    unit_price = models.FloatField(default=0)
    
    def get_absolute_url(self):
        return "/ingredient/list"

class MenuItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.00)
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
