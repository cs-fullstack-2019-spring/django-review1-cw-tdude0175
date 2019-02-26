from django.db import models

# Create your models here.


class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    alcoholPercent = models.IntegerField(default=0)
    servingGlass = models.CharField(max_length=100)

    def __str__(self):
        return self.name