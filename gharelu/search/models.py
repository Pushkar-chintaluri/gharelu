from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name_vc = models.CharField(max_length=100)
    food_group_vc = models.CharField(max_length=100)

    def __repr__(self):
        return self.name_vc

    def __str__(self):
        return self.name_vc

class Recipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    name_vc = models.CharField(max_length=100)


    def __repr__(sslf):
        return self.name_vc

    def __str__(self):
        return self.name_vc

