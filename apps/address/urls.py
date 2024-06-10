from django.urls import path
from .views import *

urlpatterns = [
    path('list', ListAddressView.as_view())
]