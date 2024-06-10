from django.urls import path
from .views import *

urlpatterns = [
    path('list', ListRoomView.as_view())
]
