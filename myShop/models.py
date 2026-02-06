from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    choice_tag = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    