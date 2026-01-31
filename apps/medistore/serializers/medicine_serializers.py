from rest_framework import serializers
from apps.medistore.models import Medicine
from apps.medistore.serializers import category_serializers, inventory_serializers

class MedicineListSerializer(serializers.ModelSerializer):
    category = category_serializers.CategorySerializer(read_only=True)
    inventory = inventory_serializers.InventorySerializer(read_only=True)

    classification_display = serializers.CharField(
        source="get_classification_display",
        read_only=True
    )
    age_group_display = serializers.CharField(
        source="get_age_group_display",
        read_only=True
    )

    class Meta:
        model = Medicine
        fields = [
            "id",
            "SKU",
            "name",
            "retail_price",
            "medicine_images",
            "is_prescription_required",
            "category",
            "classification",
            "classification_display",
            "age_group",
            "age_group_display",
            "salt_composition",
            "dosage_strength",
            "manufacturer",
            "manufacture_date",
            "expiry_date",
            "description",
            "inventory",
            "is_active",
            "created_at",
        ]
