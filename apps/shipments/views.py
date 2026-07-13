from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Shipment

from .serializers import ShipmentTrackerSerializer



class CustomerShipmentViewSet(ReadOnlyModelViewSet):
    """
    ویو فقط خواندنی (ReadOnly) برای اینکه کاربران وضعیت مرسوله خود را تعقیب کنند.
    """
    serializer_class = ShipmentTrackerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # هر کاربر فقط مرسوله‌ای را می‌بیند که فاکتور آن متعلق به خودش است
        return Shipment.objects.filter(order__customer__user=self.request.user)
        
        
    
