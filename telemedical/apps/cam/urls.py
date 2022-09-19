from django.urls import path
from . import views

urlpatterns = [
    path('', views.meeting, name='meeting'),
]