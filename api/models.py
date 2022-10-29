from django.db import models

class Api(models.Model):
    name = models.CharField(max_length=500)
    brand = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField()
    # price = models.IntegerField(default=0)
    # currency = models.CharField(max_length=20)
    # in_stock = models.CharField(max_length=10)
    # gender = models.BooleanField()
    # quantity = models.IntegerField(default=0)


    def __str__(self):
        return self.name

