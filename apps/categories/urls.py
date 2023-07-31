from django.urls import path
from . import views
 
# Aqui defino todas las url que estan en categories
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about,name = 'about' ),
    path('category_list/', views.category_list, name = 'category_list'),    
    path('category_create/', views.category_create, name='category_create'),
    path('product_list/', views.product_list, name = 'product_list'),    
    path('product_create/', views.product_create, name='product_create'),
    path('product_read/<id>/', views.product_read, name='product_read'),   
    path('product_update/<id>/', views.product_update, name='product_update'),
    path('product_delete/<id>/', views.product_delete, name='product_delete'),
]