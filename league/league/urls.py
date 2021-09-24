from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('tournaments.urls')),
    url(r'^create_tour/', include('tournaments.urls')),
    url(r'^accounts/', include('accounts.urls')),
]
