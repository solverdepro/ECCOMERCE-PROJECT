from django.db import models
from django.urls import reverse

class cartegory(models.Model):
    cartegory_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    carteg_image = models.ImageField(upload_to='photos/cartegories', blank=True)

    class Meta:
        verbose_name = 'cartegory'
        verbose_name_plural = 'cartegories'
    
    def get_url(self):
        return reverse('products_by_cartegory', args = [self.slug])

    def __str__(self):
        return self.cartegory_name
