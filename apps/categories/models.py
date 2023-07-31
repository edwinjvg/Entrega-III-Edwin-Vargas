from django.db import models
# Esta es la clase padre para los productos
class Category(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['name']
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")    
        
    def __str__(self):
        return self.name
# Clase prodcuto con una llave foranea que lo asocia a la categoria        
class Product(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=2000, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    image = models.ImageField(blank = True, upload_to = 'img/')
    
    class Meta:
        ordering = ["-title"]
    
    def __str__(self):
        return self.title
