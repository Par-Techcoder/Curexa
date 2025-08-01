from apps.core.models.base_model import BaseModel
from django.db import models

class Users(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    
    
