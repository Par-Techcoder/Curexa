from django.db import models

class AddressModel(models.Model):
       
    house_number = models.CharField(max_length=100)   
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    is_default = models.BooleanField(default=False)

    class Meta:
        abstract = True
        
