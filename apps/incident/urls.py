from django.urls import path
from .views import *

urlpatterns = [
    path('list', ListIncidentView.as_view())
]
