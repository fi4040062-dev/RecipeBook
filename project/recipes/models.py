from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField(blank=True)
    image = models.ImageField(upload_to='food_images')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    




# Create your models here.
