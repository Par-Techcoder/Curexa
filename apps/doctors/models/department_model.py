from django.db import models
from apps.core.models.base_model import BaseModel

class Department(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    head = models.ForeignKey(
        'doctors.DoctorProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_departments'
    )

    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'departments'
        ordering = ['name']

    def __str__(self):
        return self.name