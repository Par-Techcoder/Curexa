from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        'accounts.User', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='fk_created_by_%(class)s_user_id'
    )
    updated_by = models.ForeignKey(
        'accounts.User', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='fk_updated_by_%(class)s_user_id'
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

