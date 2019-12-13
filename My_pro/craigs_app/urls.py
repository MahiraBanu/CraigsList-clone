from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home page'),
    path("search/", views.new_search, name='new_search'),
]