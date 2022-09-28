from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250,
                            db_index=True)
    name_ru = models.CharField(max_length=250)
    name_en = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    slug = models.SlugField(max_length=50,
                            unique=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class City(models.Model):
  name = models.CharField(max_length=250,
                              db_index=True)
  slug = models.SlugField(max_length=50,
                              unique=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'city'
    verbose_name_plural = 'city'

  def __str__(self):
     return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, db_index=True)
    name_ru = models.CharField(max_length=250, blank=True)
    name_en = models.CharField(max_length=250, blank=True)
    adress = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, db_index=True)
    image1 = models.ImageField(upload_to='products/%y/%m/%d', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/%y/%m/%d', blank=True, null=True)
    adress = models.CharField(max_length=250, blank=True)
    number_company = models.CharField(max_length=12, default='+998')
    description = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    price = models.CharField(max_length=250)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
