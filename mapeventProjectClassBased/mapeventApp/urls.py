#pylint:disable=E0001
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views,home
from mapeventApp.events_form import addevent,showbookings,staffrequest
from mapeventApp.registration_view import usercreate,superusercreate
from mapeventApp.events_view import createevent,updateevent,deleteevent,listevent,detailevent
from .views import changePassword

urlpatterns = [

   path('logininfo',usercreate.UserCreate.as_view(), name='sign'),
   path('superuser-registration',superusercreate.SuperUserCreate.as_view(), name='superusersign'),
#   path('login',views.sign, name='login'),
   path('map',listevent.ListEventHome.as_view(), name='map'),
   path('searchdetail',views.searchDetail, name='searchdetail'),
   path('event/<pk>',detailevent.DetailEvent.as_view(), name='detailevent'),
   path('update/<pk>',updateevent.UpdateEvent.as_view(), name='updateevent'),
   path('delete/<pk>',deleteevent.DeleteEvent.as_view(), name='deleteevent'),
   path('',listevent.ListEventHome.as_view(), name='map'),
   path('listevent',listevent.ListEventForEditDelete.as_view(), name='listevent'),
   path('pass',changePassword.as_view(template_name='changePassword.html')),
 #  path('set',changePassword.as_view(template_name='resatePassword.html')),
   path('password_success',views.password_success, name='password_success'),
   path('personaldetails',views.personalDetails, name='personaldetails'),
   # path('eventform',bookevents.events, name='eventform'),
  path('adminlogin',views.adminlogin, name='admin'),

  path('booking',showbookings.booking, name='booking'),
  path('request',staffrequest.request, name='request'),
  path('staffdata',views.staffinfo, name='staffdata'),
   path('forgotPassword',views.forgotpassword, name='forgotpassword'),
   path('reset_password_success',views.reset_password_success, name='reset_password_success'),
   path('reset_password_success/<uidb64>/<token>',views.resetpasswordlink, name='reset_password_success'),
   path('addevent',createevent.CreateEvent.as_view(), name='eventadd'),
   path('gotologin',views.gotologin, name='gotologin'),
   path('activate/<uidb64>/<token>',views.activate, name='activate'),

]

