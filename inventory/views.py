from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, F
from django.urls import reverse_lazy
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement

from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm

# Create your views here.


def home(request):
   return render(request, 'inventory/home.html')

# Ingredient CRUD

class IngredientList(ListView):
   model = Ingredient
   template_name="inventory/ingredient/ingredient.html"
   

class IngredientCreate(CreateView):
   model = Ingredient
   template_name = "inventory/ingredient/ingredient_create.html"
   form_class = IngredientForm

   
class IngredientUpdate(UpdateView):
   model = Ingredient
   template_name = "inventory/ingredient/ingredient_update.html"
   form_class = IngredientForm


class IngredientDelete(DeleteView):
   model = Ingredient
   template_name = "inventory/ingredient/ingredient_confirm_delete.html"
   success_url = reverse_lazy('ingredientlist')
   
# MenuItem CRUD

class MenuItemList(ListView):
   model = MenuItem
   template_name = "inventory/menuitem/menuitem.html"


class ReportView(TemplateView):
   template_name="inventory/reports.html"
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["purchases"] = Purchase.objects.all()
      revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
      total_cost = 0
      for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
               total_cost += recipe_requirement.ingredient.unit_price* \
                  recipe_requirement.quantity

      context["revenue"] = revenue
      context["total_cost"] = total_cost
      context["profit"] = revenue - total_cost

      return context

class MenuItemCreate(CreateView):
   model = MenuItem
   template_name = "inventory/menuitem/menuitem_create.html"
   fields = ["title","price"]


class MenuItemUpdate(UpdateView):
   model = MenuItem
   template_name = "inventory/menuitem/menuitem_update.html"
   fields = ["title","price"]


class MenuItemDelete(DeleteView):
   model = MenuItem
   template_name = "inventory/menuitem/menuitem_delete.html"
   
# Purchases

class PurchaseList(ListView):
   model = Purchase
   template_name = "inventory/purchase/purchase.html"


class PurchaseCreate(CreateView):
   model = Purchase
   template_name = "inventory/purchase/purchase_create.html"
   fields = ["menu_item"]


class PurchaseUpdate(UpdateView):
   model = Purchase
   template_name = "inventory/purchase/purchase_update.html"
   fields = ["menu_item"]


class PurchaseDelete(DeleteView):
   model = Purchase
   template_name = "inventory/purchase/purchase_delete.html"
   
# Purchases

class RecipeRequirementList(ListView):
   model = RecipeRequirement
   template_name = "inventory/menuitem/reciperequirement.html"
