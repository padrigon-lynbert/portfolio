from django.urls import path
from .views import index

urlpatterns = [
    path('dashboard', index, name='index')
]