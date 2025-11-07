from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

