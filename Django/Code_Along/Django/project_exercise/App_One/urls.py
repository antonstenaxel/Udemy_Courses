from django.conf.urls import url,include
from App_One import views

urlpatterns = [
    url(r'^$', views.users)

]
