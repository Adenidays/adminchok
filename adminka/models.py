from django.db import models
from django.urls import reverse
from datetime import date


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length = 50)
    price = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    date = models.DateField(default=date.today)

    def __str__(self) -> str:
        return f"{self.name} - {self.price}"
    

    def get_absolute_url(self):
        return reverse('user:prodd', args=[self.pk, ])
    