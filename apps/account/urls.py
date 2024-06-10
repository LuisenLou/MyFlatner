from django.urls import path
from .views import *

urlpatterns = [
    path('list', ListAccountView.as_view())
]