from django.urls import path
from . import views

urlpatterns = [

    path('',views.event_login , name='event_login'),
    path('event_logout',views.event_logout , name='event_logout'),

    path('register/',views.register,name='register'),


    path('index/',views.index,name='index'),
     path('about/',views.about,name='about'),
     path('events/',views.events,name='events'),
     path('bookings/',views.bookings,name='bookings'),
     path('contact/',views.contact,name='contact'),
     path('sucess/',views.sucess,name='sucess'),
     path('appoiments/',views.appoiments,name='appoiments'),
     

    #  admin

    path('admin_home/',views.admin_home,name='admin_home'),


    


]