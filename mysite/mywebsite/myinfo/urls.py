from django.conf.urls import url,include
from . import views


urlpatterns = [

    url(r'^$', views.Home.as_view(),name='home'),
    url(r'^about/', views.AboutMe.as_view(),name='about'),
    url(r'^userinfo/', views.CreatePostView.as_view(),name='user'),
        url(r'^comments/', views.DataListView.as_view(),name='list'),





]
