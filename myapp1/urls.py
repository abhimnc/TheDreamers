from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import os

from . import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
    url(r'^myapp1/list1/$', views.list, name='list1'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
