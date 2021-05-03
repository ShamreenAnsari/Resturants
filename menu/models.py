from django.db import models


from django.urls import reverse

# Create your models here.
#modelname->singular
#table name-->pluarl
class menu(models.Model):
    number=models.IntegerField()
    name=models.CharField(max_length=30)
    price=models.IntegerField()

    def __str__(self):
        return self.name
    
