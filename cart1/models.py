from django.db import models

class Cart(models.Model):
    productname=models.CharField(max_length=200)
    itemprice=models.IntegerField()
    quantity=models.IntegerField()
    itemid=models.PositiveIntegerField(primary_key=True)
    
    def __str__(self):
        return self.productname[0:50]

    
