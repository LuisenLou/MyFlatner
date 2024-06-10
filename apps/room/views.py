from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Room

# Create your views here.


class ListRoomView(APIView):
    permission_classes = (permissions.AllowAny)
    permission_classes = (permissions.IsAuthenticated)

    def get(self, request, format =None):
        if Room.objects.all().exists():
            rooms = Room.objects.all()

            result = []

            for room in rooms:
                item = {}
                item['id']
                item['title'] = room.title
                item['description'] = room.description
                item['month_price'] = room.month_price
                item['room_class'] = room.room_class
                item['photos'] = room.photos
                item['available'] = room.available
                item['available_date'] = room.available_date

            result.append(item)

            return Response({'Room': result}, status = status.HTTP_200_OK)
        else:
            return Response({'error': 'No rooms found'}, status=status.HTTP_404_NOT_FOUND)
