from django.conf.urls import url
from . import views

app_name = 'tournaments'

urlpatterns = [
    url(r'^$', views.tours_view, name='tours'),
    url(r'^create_tour/', views.create_tour, name='create_tour'),
]