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

# Product
class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "product_imgs/")
    slug = models.CharField(max_length=500)
    detail = models.TextField()
    specification = models.TextField()
    price = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title