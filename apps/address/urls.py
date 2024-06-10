from django.urls import path
from .views import *

urlpatterns = [
    path('List', ListAddressView.as_view())
]