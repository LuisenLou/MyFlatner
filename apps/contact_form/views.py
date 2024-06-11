from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Contact_form
from .serializer import ContactFormSerializer

class ContactFormView(APIView):
    permission_classes = (permissions.AllowAny,) 
    #permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        if Contact_form.objects.all().exists():
            contact_forms = Contact_form.objects.all()
            serializer = ContactFormSerializer(contact_forms, many=True)
            return Response({'Contact_forms': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No contact forms found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
