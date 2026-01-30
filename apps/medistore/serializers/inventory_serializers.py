from rest_framework import serializers
from apps.medistore.models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["change_quantity"]