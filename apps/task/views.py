from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Task

# Create your views here.

class ListTaskView(APIView):
    permission_classes = (permissions.AllowAny,)
    #permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):

        if Task.objects.all().exists():
            tasks = Task.objects.all()

            result = []

            for task in tasks:
                item = {}
                item['id'] = task.id
                item['title'] = task.title
                item['status'] = task.status
                item['task_date'] = task.task_date
                item['task_limit_date'] = task.task_limit_date

            result.append(item)

            return Response({'Tasks': result}, status = status.HTTP_200_OK)
        else:
            return Response({'error': 'No tasks found'}, status=status.HTTP_404_NOT_FOUND)
