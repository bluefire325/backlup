from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('(P<events_id>[0-9]+)/', views.detail, name='detail'),

    path('signup/', views.SignUp.as_view(), name='signup'),
    path('index/',views.index, name='index')


   

]