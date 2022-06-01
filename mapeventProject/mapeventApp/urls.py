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
   path('map.html',views.map, name='map'),
   path('',views.map, name='map'),
 path('map.html',views.map, name='map'),
   path('pass.html',changePassword.as_view(template_name='changePassword.html')),
 #  path('set',changePassword.as_view(template_name='resatePassword.html')),
   path('password_success',views.password_success, name='password_success'),
   path('personalDetails.html',views.personalDetails, name='personalDetails'),
   path('eventForm1.html',views.event1, name='eventForm'),
  path('booking.html',views.booking, name='booking'),
  path('booking',views.booking, name='booking'),
  path('booking2.html',views.booking, name='booking'),
   path('eventForm2.html',views.event2, name='eventForm'),
   path('eventForm3.html',views.event3, name='eventForm'),
   path('eventForm4.html',views.event4, name='eventForm'),
   path('eventForm5.html',views.event5, name='eventForm'),
   path('eventForm6.html',views.event6, name='eventForm'),
   path('logout',views.logoutuser, name='logout'),
   path('forgotPassword.html',views.forgotpassword, name='forgotpassword'),
   path('reset_password_success',views.reset_password_success, name='reset_password_success'),
   path('reset_password_success/<uidb64>/<token>',views.resetpasswordlink, name='reset_password_success'),
   path('addevent.html',views.addevent, name='eventadd'),
   path('gotologin.html',views.gotologin, name='gotologin'),
   path('activate/<uidb64>/<token>',views.activate, name='activate'),
#   path('forgotPassword.html',views.forgotPassword, name='forgotPassword'),


]

