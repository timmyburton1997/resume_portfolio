from . import views
from django.urls import path


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_id>/', views.detail, name='detail')

]