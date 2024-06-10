from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Address

# Create your views here.


class ListAddressView(APIView):
    permission_classes = (permissions.AllowAny,)
    #permission_classes = (permissions.IsAuthenticated)

    def get(self, request, format = None):
        if Address.objects.all().exists():
            addresses = Address.objects.all()

            result = []
 
            for address in addresses:
                item = {}
                item['id'] = address.id
                item['via_class'] = address.via_class
                item['via_name'] = address.via_name
                item['via_number'] = address.via_number
                item['floor'] = address.floor
                item['door'] = address.door
                item['postal_code'] = address.postal_code
                item['city'] = address.city
                item['province_or_state'] = address.province_or_state
                item['country'] = address.country

            result.append(item)

            return Response({'Addresses': result}, status = status.HTTP_200_OK)
        else:
            return Response({'error': 'No address found'}, status=status.HTTP_404_NOT_FOUND)