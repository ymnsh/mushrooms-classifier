from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recognise/', views.api_recognise, name='api'),
    url(r'^$', views.index, name='index')
]