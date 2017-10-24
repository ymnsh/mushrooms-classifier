from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^handler/', views.index, name='handler'),
    url(r'^$', views.index, name='index')
]