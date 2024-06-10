from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Flat

# Create your views here.


class ListFlatView(APIView):
    permission_classes = (permissions.AllowAny,)
    #permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format = None):
        if Flat.objects.all().exists():
            flats = Flat.objects.all()

            result = []
 
            for flat in flats:
                item = {}
                item['id'] = flat.id
                item['title'] = flat.title
                item['description'] = flat.description
                item['published'] = flat.published
                item['num_rooms'] = flat.num_rooms
                item['num_bathrooms'] = flat.num_bathrooms
                item['area'] = flat.area
                item['renovated'] = flat.renovated
                item['elevator'] = flat.elevator
                item['latitude'] = flat.latitude
                item['longitude'] = flat.longitude
                item['photos'] = flat.photos
                item['views'] = flat.views

            result.append(item)

            return Response({'Flats': result}, status = status.HTTP_200_OK)
        else:
            return Response({'error': 'No flats found'}, status=status.HTTP_404_NOT_FOUND)
