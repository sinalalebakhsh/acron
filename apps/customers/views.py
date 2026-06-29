from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomerSerializer


class CustomerMeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = CustomerSerializer(request.user.customer)

        return Response(serializer.data)





