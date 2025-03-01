from django.urls import path
from . import views

urlpatterns = [
    path('',views.shp_login, name='shp_login'),
    path('shp_login1/', views.shp_login1, name='shp_login1'),
    path('shp_logout/',views.shp_logout, name='shp_logout'),

    path('admin_home/', views.admin_home, name='admin_home'),


    path('register/', views.register, name='register'),
    path('user_home', views.user_home, name='user_home'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),

     path('user_home1', views.user_home1, name='user_home1'),
    path('admin_bookings/', views.admin_bookings, name='admin_bookings'),
    path('delete_bookings/<int:appointment_id>/', views.delete_bookings, name='delete_bookings'),


    path('booking/', views.booking, name='booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('view_bookings/', views.view_bookings, name='view_bookings')

]