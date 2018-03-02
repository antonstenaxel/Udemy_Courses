from django.conf.urls import url
from App_One import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
