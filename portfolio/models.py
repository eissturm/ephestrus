from django.db import models
from markupfield.fields import MarkupField

# Create your models here.
class PortItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    description = MarkupField(default_markup_type='markdown')
    img = models.ImageField(upload_to='portfolio')

class Site(PortItem):
    client = models.CharField(max_length=150)
    services = models.CharField(max_length=75)

class App(PortItem):
    pass