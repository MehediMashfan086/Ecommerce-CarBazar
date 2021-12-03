from django.db import models

# Category
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "category_imgs/")
    
    class Meta:
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.title
    
# Brand
class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "brand_imgs/")
    
    def __str__(self):
        return self.title
    
# Color
class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

# Size
class Size(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title