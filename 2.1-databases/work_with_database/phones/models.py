from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля

    name = models.CharField(max_length=50)
    price = models.IntegerField()   #DecimalField
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

