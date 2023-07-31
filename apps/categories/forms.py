from .models import Category, Product
from django.forms import ModelForm
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )
# Formulario que nos permitira crear categorias
class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Pais Destino ',
        }       
# este modelo es para la creacion de productos
class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'content', 'category', 'image')
        labels = {
            'title': 'Destino ',
            'content': 'Detalle Destino ',
            'category': 'Pais ',
            'image': 'Imagen ',
        }       
# este modelo es para poder editar un productos
class UpdateProductForm(ModelForm):
    class Meta:
        model = Product
        fields =  ('title', 'content', 'category', 'image')
        labels = {
            'title': 'Destino ',
            'content': 'Detalle Destino ',
            'category': 'Pais ',
            'image': 'Imagen ',
        } 