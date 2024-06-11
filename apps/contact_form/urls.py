from django.urls import path
from .views import *

urlpatterns = [
    path('api/contact/', ContactFormView.as_view()),
]
