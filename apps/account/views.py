from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Account

# Create your views here.

class ListAccountView(APIView):
    permission_classes = (permissions.AllowAny,)
    #permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):

        if Account.objects.all().exists():
            accounts = Account.objects.all()

            result = []

            for account in accounts:
                item = {}
                item['id'] = account.id
                item['username'] = account.username
                item['birth_date'] = account.birth_date
                item['genre'] = account.genre
                item['country'] = account.country
                item['province_or_state'] = account.province_or_state
                item['city'] = account.city
                item['ocupation'] = account.ocupation
                item['profile_photo'] = account.profile_photo
                item['description'] = account.description
                item['role'] = account.role

            result.append(item)

            return Response({'Incidents': result}, status = status.HTTP_200_OK)
        else:
            return Response({'error': 'No tasks found'}, status=status.HTTP_404_NOT_FOUND)