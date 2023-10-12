from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, null=False)
    price = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title

