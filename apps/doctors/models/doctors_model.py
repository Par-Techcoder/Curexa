from apps.core.models.base_model import BaseModel
from django.db import models

class Doctors(BaseModel):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    
    class Meta:
        db_table = 'doctors'
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        ordering = ['name']
    
    def __str__(self):
        return self.name
