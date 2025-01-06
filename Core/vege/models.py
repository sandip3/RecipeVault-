from django.db import models
# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField( max_length=100)
    recipe_desription = models.TextField()
    recipe_img = models.ImageField(upload_to='recipe')

    def __str__(self):
        return self.recipe_name
    
