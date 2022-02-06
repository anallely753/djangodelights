from django.shortcuts import render
from django.http import HttpResponse

from .models import Ingredient

from django.views.generic import ListView

# Create your views here.


def home(request):
   return render(request, 'inventory/home.html')

class IngredientList(ListView):
   model = Ingredient
   template_name="inventory/ingredient.html"