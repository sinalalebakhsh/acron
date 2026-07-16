from rest_framework import serializers
from .models import Shipment

class ShipmentTrackerSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    carrier_display = serializers.CharField(source='get_carrier_display', read_only=True)
    tracking_url = serializers.CharField(source='get_tracking_url', read_only=True)

    class Meta:
        model = Shipment
        fields = [
            'id', 'status', 'status_display', 'carrier', 
            'carrier_display', 'tracking_number', 'tracking_url',
            'created_at', 'shipped_at', 'delivered_at'
        ]
        
        
