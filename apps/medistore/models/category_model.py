from django.db import models
from apps.core.models.base_model import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)    
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name} | Description: {self.description[:50]} | Active: {self.is_active}"
    