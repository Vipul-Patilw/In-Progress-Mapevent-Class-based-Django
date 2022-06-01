#pylint:disable=E0602
#pylint:disable=E0001
from quopri import decodestring
from django.shortcuts import redirect, render
from mapeventApp.models import  Event, Login,ForgotPassword
from mapeventApp.event import events
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from mapeventProject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from mapeventApp.models import AddEvent
from . tokens import generate_token
from django.core.mail import EmailMessage

# Create your views here.


class changePassword(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')

def password_success(request):
	messages.info(request,"Password Changed Successfully")
	return render (request, 'personalDetails.html')


def index(request):
		if request.method =="POST":
		
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			mobile_number= request.POST.get('mobile_number')
			username= request.POST.get('username')
			email = request.POST.get('email')
			password= request.POST.get('password')
			gender = request.POST.get('gender')
			birthdate = request.POST.get('birthdate')
			password2 = request.POST.get('password2')
			
		
			if User.objects.filter(email=email):
						messages.error(request,"this email address already registered with us try different email address")
						return redirect("/sign")
						
			if User.objects.filter(username=username):
						messages.error(request,"this username is already exist try another")
						return redirect("/sign")

			if password != password2:
				messages.error(request,"confirm password doesn't matched with the password")
				return redirect ('/sign')
				
			if len(password)>=6 and re.search(r"[A-Z][a-z]+[@_!#$%^&*()?/}{~:]+[0-9]",password):
				pass
				
			else:
				messages.error(request,"password should be at least 6 character long. contain both uppercase and lowercase character, at least one alpha numeric and one special charecter  (eg:Test@123)")
				return redirect("/sign")
				

			messages.success(request, first_name.title() + " " + last_name.title())
			myuser = User.objects.create_user(username,email,password)
			myuser.first_name = first_name
			myuser.last_name = last_name
			myuser.is_active = False
			myuser.save()	
			
			users = Login(first_name=first_name,username=username, mobile_number=mobile_number,last_name=last_name,email=email,birthdate=birthdate,gender=gender,)
			users.save()		
			
			#confirmation email
			current_site = get_current_site(request)
			email_sub2 = 'Activate your MCCIA Account'
			message2 = render_to_string('email_confirmation.html',{
				'fname': myuser.first_name,
				'lname': myuser.last_name, 
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
				'token': generate_token.make_token(myuser)
				})
			email = EmailMessage(
				email_sub2,
				message2,
				settings.EMAIL_HOST_USER,
				[myuser.email],
				)
			
			email.fail_silently= True
			email.send()

			
			return render(request, 'gotologin.html')
					
					
			
		#	except:
			#	messages.error(request,"some problem come in our application please reopen the application")
			#	return redirect ('/sign')
				
		#return render(request, 'logininfo.html')	
		return render(request, 'logininfo.html')
	
	#  return HttpResponse("vipul patil")

def gotologin(request):
	return render (request,'gotologin.html')	
def sign(request):

	if request.method =="POST":
		Loginpassword= request.POST.get('Loginpassword')
		username = request.POST.get('username')
		user = authenticate(username=username, password=Loginpassword)
		if user is not None:
			
			login(request, user)
			return redirect('/map')
			#full_name = user.first_name
		
		

		else:
	#	if str(Loginpassword) == str(b):
		#	messages.error(request,"password matched")
		#	return redirect('/login')    			
	  
			messages.error(request, "Please enter correct username and  password ")
			return redirect('/login')    
		#	return render(request,'index.html')   
	return render(request,'index.html')


	
def setting(request):
	return render (request,'setting.html')
		


def personalDetails (request):
	return render (request,'personalDetails.html')
	



def logoutuser(request):
	logout(request)
	return redirect ("/login")

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

def addevent(request):
	if request.method =="POST":
		event = request.POST.get('event')
		info = request.POST.get('info')
		eventaddress = request.POST.get('eventaddress')
		date = request.POST.get('date')
		time = request.POST.get('time')
		lang = request.POST.get('lang')
		lat = request.POST.get('lat')
		maping = AddEvent(event=event,info=info,lang=lang,lat=lat,eventaddress=eventaddress,date=date,time=time)
		maping.save()

		#maping1 = {'event1':event,'info':info,'lang':lang,'lat':lat}
		return  redirect('/map')
	return render (request, 'addevent.html')




def map(request):
	if request.user.is_anonymous:
			return redirect ("/login")
	maping = AddEvent.objects.all()
	maping1 = {'mapings':maping}
	return render (request,'map.html',maping1)


def event1(request):
	if request.method =="POST":
		events(request)
		return redirect("/booking")
	return render (request,'eventForm1.html')

def event2(request):
	if request.method =="POST":
		events(request)
		return redirect("/booking")
	return render (request,'eventForm2.html')

def event3(request):
	if request.method =="POST":
		events(request)
		return redirect("/booking")
	return render (request,'eventForm3.html')

def event4(request):
	if request.method =="POST":
		events(request)
		return redirect("/booking")
	return render (request,'eventForm4.html')

def event5(request):
	if request.method =="POST":
		events(request)
		return redirect("/booking")
	return render (request,'eventForm5.html')

def event6(request):
	if request.method =="POST":
		events(request)
		return redirect("/booking")
	return render (request,'eventForm6.html')

def booking(request):
	if request.method =="POST":
		email = request.POST.get('email')
		events = Event.objects.filter(email=email).all()
		return render (request,'booking2.html', {'events':events})
	return render (request,'booking.html')

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

	
