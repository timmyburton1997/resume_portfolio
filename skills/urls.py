from . import views
from django.urls import path


urlpatterns = [
    path('',views.skills, name = 'skills')
]