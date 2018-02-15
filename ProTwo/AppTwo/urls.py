from django.conf.urls import url
from AppTwo import views
urlpatterns = [

    url(r'^$',views.AppTwo.help,name='help'),

]
