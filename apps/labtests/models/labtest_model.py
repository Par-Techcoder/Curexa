from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import TEST_CATEGORY

class MedicalTest(BaseModel):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=TEST_CATEGORY)
    price = models.DecimalField(max_digits=10, decimal_places=2)    

    class Meta:
        db_table = 'medical_tests'
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"
