from django.db import models

# Create your models here.

class Products(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.BigIntegerField(max_length=255)
    photo = models.ImageField(upload_to=None, max_length=100, height_field=None, width_field=None)
    def __str__(self) -> str:
        return self.Name