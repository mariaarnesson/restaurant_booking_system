from django.db import models
from cloudinary.models import CloudinaryField


class Menu(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Meal(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)    
    mealName = models.CharField(max_length=100)
    mealDescription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.mealName

class Drink(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    drinkName = models.CharField(max_length=100)
    drinkDescription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.drinkName
            