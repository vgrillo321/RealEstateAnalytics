from django.db import models

# Create your models here.

class RentalProperties(models.Model):


    address=models.CharField(max_length=150)
    price=models.CharField(max_length=500)
    size=models.CharField(max_length=500)
    pricePerSqft=models.CharField(max_length=500)

    # string representation of the class
    # def __str__(self):
        
    #     #it will return the title
        
    #     return self.address