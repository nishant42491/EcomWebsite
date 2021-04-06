from django.db import models

# Create your models here.

class Products(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    
    def __str__(self):
        return self.title[0:50]


    def get_absolute_url(self):
        pass
