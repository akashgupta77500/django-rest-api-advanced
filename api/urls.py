
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('api', views.api, name='api'),
    path('api/<int:pk>', views.api, name='api'),
]