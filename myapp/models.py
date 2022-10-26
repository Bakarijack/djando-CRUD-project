from email.policy import default
from unicodedata import category
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 255, default = '')

    def __str__(self) -> str:
        return self.title

class Flower(models.Model):
    title = models.CharField(max_length = 255, default = '')
    description = models.TextField(default='')
    slug = models.SlugField(blank = True, default = '')
    category = models.ForeignKey(Category, null=True, on_delete = models.PROTECT)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Flower, self).save()

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.slug)])
    
