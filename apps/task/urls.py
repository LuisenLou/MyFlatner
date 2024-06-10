from django.urls import path
from .views import *

urlpatterns = [
    path('list', ListTaskView.as_view())
]