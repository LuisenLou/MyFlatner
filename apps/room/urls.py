from django.urls import path
from .views import *

urlpatterns = [
    path('List', ListRoomView.as_view())
]
