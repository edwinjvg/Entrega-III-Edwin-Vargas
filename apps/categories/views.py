from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import *
from django.contrib import messages
# definimos el inicio
def home(request):
    return render(request, 'categories/home.html')
# definimos el quien somos
def about (request):
    return render(request, 'categories/about.html')
# listamos todos las categorias
def category_list (request):
    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }
    return render(request, 'categories/category_list.html', context)
# creamos todos las categorias
def category_create(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, request.FILES )
        if form.is_valid:
            try:
                form.save()
                return redirect('category_list')
            except:
                messages(request, 'Hay un error en los datos suministrados')
    else:
        form = CreateCategoryForm()    
    return render(request, 'categories/category_create.html', {"form":form})

# aqui listamos todos los productos
def product_list(request):
    products = Product.objects.order_by('-title')
    context = {
        'products': products,
    }
    return render(request, 'categories/product_list.html', context)
# Buscamos un producto segun su id.
def product_read(request, id):
    products = Product.objects.get(pk = id)
    context = {'products': products}
    return render(request, 'categories/product_read.html', context)
# Creamos un producto con el modelo creado en forms.py
def product_create(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES )
        if form.is_valid:
            try:
                form.save()
                return redirect('product_list')
            except:
                messages(request, 'Hay un error en los datos suministrados')
    else:
        form = CreateProductForm()    
    return render(request, 'categories/product_create.html', {"form":form})
# Editamos un producto con el modelo creado en forms.py segun el id seleccionado
def product_update(request, id):
    products = Product.objects.get(pk = id)
    form = UpdateProductForm(instance = products)
    if request.method == 'POST':
        form = UpdateProductForm(request.POST, request.FILES, instance = products)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {'form': form}
    return render(request, 'categories/product_update.html', context)
# Eliminamos un producto con el id seleccionado
def product_delete(request, id):
    products = Product.objects.get(pk = id)
    if request.method == 'POST':
        products.delete()
        return redirect('home')
    context = {'products': products}
    return render(request, 'categories/product_delete.html', context)
