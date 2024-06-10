from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Incident

# Create your views here.

class ListIncidentView(APIView):
    permission_classes = (permissions.AllowAny,)
    #permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):

        if Incident.objects.all().exists():
            incidents = Incident.objects.all()

            result = []

            for incident in incidents:
                item = {}
                item['id'] = incident.id
                item['title'] = incident.title
                item['description'] = incident.description
                item['incident_status'] = incident.incident_status
                item['incident_date'] = incident.incident_date

            result.append(item)

            return Response({'Incidents': result}, status = status.HTTP_200_OK)
        else:
            return Response({'error': 'No tasks found'}, status=status.HTTP_404_NOT_FOUND)