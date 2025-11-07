from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import DosageForm, AGE_GROUP

class Medicine(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    medicine_image = models.ImageField(upload_to='static/images/medicines/', blank=True, null=True)
    category = models.ForeignKey(
        'medistore.Category',
        on_delete=models.CASCADE,
        related_name='fk_category_medicines_category_id'
    )
    classification = models.IntegerField(
        choices=[(tag.value, tag.name) for tag in DosageForm],
        default=DosageForm.TABLET.value, 
        null=False, blank=False
    )
    age_group = models.IntegerField(
        choices=[(group.name, group.value) for group in AGE_GROUP],
        default=AGE_GROUP.ADULT.value, 
        null=False, blank=False
    )
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    
    class Meta:
        db_table = 'medicines'
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'
        
    def __str__(self):
        return f"{self.name} | Price: ₹{self.price} | Active: {self.is_active}"
