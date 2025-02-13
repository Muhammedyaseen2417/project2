from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
     path('about/',views.about,name='about'),
     path('events/',views.events,name='events'),
     path('bookings/',views.bookings,name='bookings'),
     path('contact/',views.contact,name='contact'),


]