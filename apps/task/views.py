from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Task

# Create your views here.

class ListTaskView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        if Task.objects.all().exists():
            return Response({'Tasks': ListTaskView}, status = status.HTTP_200_OK)
        else:
            return Response({'error': 'No tasks found'}, status=status.HTTP_404_NOT_FOUND)
