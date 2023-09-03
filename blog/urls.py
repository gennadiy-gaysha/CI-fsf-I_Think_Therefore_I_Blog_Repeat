from . import views
from django.urls import path

urlpatterns = [path('', views.ListView.as_view(), name='home'),]