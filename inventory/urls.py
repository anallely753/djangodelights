from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ingredient/list', views.IngredientList.as_view(),name="ingredientlist"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
    path("ingredient/<pk>", views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredientdelete"),
    
    path('menuitem/list', views.MenuItemList.as_view(),name="menuitemlist"),
    path("menuitem/create", views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path("menuitem/<pk>", views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path("menuitem/delete/<pk>", views.MenuItemDelete.as_view(), name="menuitemdelete"),
    
    path('purchase/list', views.PurchaseList.as_view(),name="purchaselist"),
    path("purchase/create", views.PurchaseCreate.as_view(), name="purchasecreate"),
    path("purchase/<pk>", views.PurchaseUpdate.as_view(), name="purchaseupdate"),
    path("purchase/delete/<pk>", views.PurchaseDelete.as_view(), name="purchasedelete"),
    
    path('reciperequirement/list/', views.RecipeRequirementList.as_view(), name="reciperequirementlist"),
    path('reports', views.ReportView.as_view(), name="reports")


]
