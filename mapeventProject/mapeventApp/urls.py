#pylint:disable=E0001
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import changePassword
urlpatterns = [
   path('sign',views.index, name='sign'),
   path('logininfo.html',views.index, name='sign'),
   path('login',views.sign, name='login'),
   path('index.html',views.sign, name='login'),
   path('map',views.map, name='map'),
   path('map.html',views.map, name='map'),  path('searchdetail',views.searchDetail, name='searchdetail'),
   path('',views.map, name='map'),
 path('map.html',views.map, name='map'),
   path('pass.html',changePassword.as_view(template_name='changePassword.html')),
 #  path('set',changePassword.as_view(template_name='resatePassword.html')),
   path('password_success',views.password_success, name='password_success'),
   path('personalDetails.html',views.personalDetails, name='personalDetails'),
   path('eventForm1.html',views.event1, name='eventForm'),
  path('booking.html',views.booking, name='booking'),
  path('adminlogin',views.adminlogin, name='admin'),
  path('adminsignIn',views.adminsign, name='adminsign'),
  path('booking',views.booking, name='booking'),
  path('request',views.request, name='request'),
  path('staffdata',views.staffinfo, name='staffdata'),
  path('deleteEvent',views.deleteEvent, name='delteEvent'),
   path('logout',views.logoutuser, name='logout'),
   path('forgotPassword.html',views.forgotpassword, name='forgotpassword'),
   path('reset_password_success',views.reset_password_success, name='reset_password_success'),
   path('reset_password_success/<uidb64>/<token>',views.resetpasswordlink, name='reset_password_success'),
   path('addevent.html',views.addevent, name='eventadd'),
   path('gotologin.html',views.gotologin, name='gotologin'),
   path('activate/<uidb64>/<token>',views.activate, name='activate'),
#   path('forgotPassword.html',views.forgotPassword, name='forgotPassword'),


]

