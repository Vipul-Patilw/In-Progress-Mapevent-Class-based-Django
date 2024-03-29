#pylint:disable=E0602
#pylint:disable=E0001
from quopri import decodestring
from django.shortcuts import redirect, render
from django.core.paginator import  Paginator
from mapeventApp.models import  Event,UserRegistration,ForgotPassword,Staff,Add,Admin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from mapeventProject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from . tokens import generate_token
from django.core.mail import EmailMessage
from django.views.generic import ListView
from .forms import AddEventForm,UserCreateForm
from .models import AddEvent
from django.views.generic.edit import CreateView,FormView,UpdateView,DeleteView


# Create your views here.

				      	
class changePassword(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')

def password_success(request):
	messages.info(request,"Password Changed Successfully")
	return render (request, 'personalDetails.html')

def gotologin(request):
	return render (request,'gotologin.html')	


def adminlogin(request):
	try:
		if request.method =="POST":
			Loginpassword= request.POST.get('Loginpassword')
			username = request.POST.get('username')
			user = authenticate(username=username, password=Loginpassword)
			
			if user is not None and user.is_superuser == True or user.is_staff == True:
				
				login(request, user)
				return redirect('/map')
				#full_name = user.first_name
			
			elif user.is_staff == False or user.is_superuser == False:
					messages.error(request, "this account don't have accessed to login as admin or staff, try using your admin or staff login account!")
						
					return redirect('/adminlogin')
			
			#	return render(request,'index.html')   
		return render(request,'Adminlogin.html')
	except:
				messages.error(request, "You enter wrong username and password")
					
				return redirect('/adminlogin')    

	
def setting(request):
	return render (request,'setting.html')
		
def personalDetails (request):
	return render (request,'personalDetails.html')


def activate(request, uidb64, token):

	uid = decodestring(urlsafe_base64_decode(uidb64))
	myuser = User.objects.get(pk=uid)


	if myuser is not None and generate_token.check_token(myuser, token):
		myuser.is_active = True
		myuser.save()
		login(request,myuser)
		return redirect('/login')
		
	else:
		return render(request, 'activation_failed.html')	
						
def searchDetail(request):
	return render (request,'searchDetail.html')
		
def forgotpassword(request):
	try:
		if request.method =="POST":
			email = request.POST.get('email')
			user = ForgotPassword(email=email)
			user.save()
			myuser = User.objects.get(email=email)
			current_site = get_current_site(request)
			email_sub2 = 'Reset Your MCCIA Account Password'
			body = render_to_string('password_resetMail.html',{
					'fname': myuser.first_name,
					'lname': myuser.last_name, 
					'domain': current_site.domain,
					'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
					'token': generate_token.make_token(myuser)
					})
			email = EmailMessage(
					email_sub2,
					body,
					settings.EMAIL_HOST_USER,
					[myuser.email],
					)
				
			email.fail_silently= True
			email.send()

			messages.info(request,"Link of recovery password has been sent to your Email address please click that link in order to change your password")
			return render(request,'forgotPassword.html')
			
		return render(request,'forgotPassword.html')
	except:
		messages.error(request,"Sorry! this email address is not registered with us")
		return render(request,'forgotPassword.html')

def resetpasswordlink(request, uidb64, token):
	uid = decodestring(urlsafe_base64_decode(uidb64))
	myuser = User.objects.get(pk=uid)
	if myuser is not None and generate_token.check_token(myuser, token):
		login(request,myuser)
		return redirect('/reset_password_success')
		
	else:
		return render(request, 'password_reset_failed.html')
	
def reset_password_success(request):
	if request.method =="POST":
		email = request.POST.get('email')
		new_password1 = request.POST.get('new_password1')
		new_password2 = request.POST.get('new_password2')
		if new_password1 != new_password2:
					messages.error(request,"confirm password doesn't matched with the password")
					return redirect ('/sign')
					
		if len(new_password1)>=6 and re.search(r"[A-Z][a-z]+[@_!#$%^&*()?/}{~:]+[0-9]",new_password1):
			user = User.objects.get(email=email)
			user.set_password(new_password1)
			user.save()
			messages.info(request,"Password has been changed successfully!!")
			logout(request)
			return redirect ("/login")
			
		else:
			messages.error(request,"password should be at least 6 character long. contain both uppercase and lowercase character, at least one alpha numeric and one special charecter  (eg:Test@123)")
			return redirect("/reset_password_success")
	return render(request,'resetPassword.html')	

def staffinfo(request):
	user = User.objects.filter(is_staff=True).all()
	return render(request,'staffdata.html',{'users':user})
