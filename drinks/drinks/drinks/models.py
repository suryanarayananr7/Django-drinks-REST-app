from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    # To show more description in admin site after creating drinks.
    def __str__(self):
        return self.name + ' ' + self.description