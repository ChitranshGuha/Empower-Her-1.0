# urls.py

from django.urls import path
from .views import available_jobs

urlpatterns = [
    path('available-jobs/', available_jobs, name='available_jobs'),
]
