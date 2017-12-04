from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^destroy$', views.destroy),
    url(r'^add$', views.add),
    url(r'^show$', views.show),
    url(r'^friends/(?P<user_id>\d+)$', views.show),
    url(r'^friends/(?P<user_id>\d+)/show$', views.show),

]