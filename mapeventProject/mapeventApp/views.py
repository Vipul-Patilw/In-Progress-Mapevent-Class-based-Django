#pylint:disable=E0602
#pylint:disable=E0001
from quopri import decodestring
from django.shortcuts import redirect, render
from mapeventApp.models import  Event, Login
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
from . tokens import generate_token
from django.core.mail import EmailMessage
from mapeventApp.event import events
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
				

			messages.success(request, first_name.title() + " " + last_name)
			myuser = User.objects.create_user(username,email,password)
			myuser.first_name = first_name
			myuser.last_name = last_name
			myuser.is_active = False
			myuser.save()	
			
			users = Login(first_name=first_name,username=username, mobile_number=mobile_number,last_name=last_name,email=email,birthdate=birthdate,gender=gender,)
			users.save()		

			#confirmation email
			current_site = get_current_site(request)
			email_sub2 = 'Activate your BANK-PAY Account'
			message2 = render_to_string('email_confirmation.html',{
				'name': myuser.first_name + myuser.last_name, 
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
		#	context={ "bank": bank_name,
		#	"mobile": mobile_number,
		#	"card":card_number}
			
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
			return render (request,'map.html')
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


def map(request):
	if request.user.is_anonymous:
			return redirect ("/login")
	return render (request,'map.html')

def event1(request):
	if request.method =="POST":
		event = request.POST.get('event')
		eventaddress = request.POST.get('eventaddress')
		dtime = request.POST.get('dtime')
		full_name = request.POST.get('full_name')
		email = request.POST.get('email')
		emailowner = request.POST.get('emailowner')
		mobile_number = request.POST.get('mobile_number')
		date = request.POST.get('date')
		time = request.POST.get('time')
		even = Event(email=email,emailowner=emailowner,mobile_number=mobile_number,full_name=full_name,eventaddress=eventaddress,event=event,date=date,time=time,dtime=dtime)
		even.save()

		messages.info(request, event)
		current_site = get_current_site(request)
		emailsub = "Event Booking Successfull"
		emailbody = render_to_string('mailsendtourself.html',{'eventaddress': eventaddress,
'domain': current_site.domain,
'name': full_name,
'event': event,
'dtime':dtime
})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [email]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
		emailsub = "User book the event"
		emailbody = render_to_string('mailsendtoOther.html',{'domain': current_site.domain,
'event': event,
'name': full_name,
'mobile': mobile_number, 
'email':email,
'datetime':date})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [emailowner]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
	
		return redirect("/booking")
	return render (request,'eventForm1.html')

def event2(request):
	if request.method =="POST":
		event = request.POST.get('event')
		eventaddress = request.POST.get('eventaddress')
		dtime = request.POST.get('dtime')
		full_name = request.POST.get('full_name')
		email = request.POST.get('email')
		emailowner = request.POST.get('emailowner')
		mobile_number = request.POST.get('mobile_number')
		date = request.POST.get('date')
		time = request.POST.get('time')
		even = Event(email=email,emailowner=emailowner,mobile_number=mobile_number,full_name=full_name,eventaddress=eventaddress,event=event,date=date,time=time,dtime=dtime)
		even.save()
		messages.info(request, event)
		current_site = get_current_site(request)
		emailsub = "Event Booking Successfull"
		emailbody = render_to_string('mailsendtourself.html',{'eventaddress': eventaddress,
'domain': current_site.domain,
'name': full_name,
'event': event,
'dtime':dtime
})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [email]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
		emailsub = "User book the event"
		emailbody = render_to_string('mailsendtoOther.html',{'domain': current_site.domain,
'event': event,
'name': full_name,
'mobile': mobile_number, 
'email':email,
'datetime':date})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [emailowner]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
	
		return redirect("/booking")
	return render (request,'eventForm2.html')

def event3(request):
	if request.method =="POST":
		event = request.POST.get('event')
		eventaddress = request.POST.get('eventaddress')
		dtime = request.POST.get('dtime')
		full_name = request.POST.get('full_name')
		email = request.POST.get('email')
		emailowner = request.POST.get('emailowner')
		mobile_number = request.POST.get('mobile_number')
		date = request.POST.get('date')
		time = request.POST.get('time')
		even = Event(email=email,emailowner=emailowner,mobile_number=mobile_number,full_name=full_name,eventaddress=eventaddress,event=event,date=date,time=time,dtime=dtime)
		even.save()
		messages.info(request, event)
		current_site = get_current_site(request)
		emailsub = "Event Booking Successfull"
		emailbody = render_to_string('mailsendtourself.html',{'eventaddress': eventaddress,
'domain': current_site.domain,
'name': full_name,
'event': event,
'dtime':dtime
})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [email]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
		emailsub = "User book the event"
		emailbody = render_to_string('mailsendtoOther.html',{'domain': current_site.domain,
'event': event,
'name': full_name,
'mobile': mobile_number, 
'email':email,
'datetime':date})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [emailowner]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
	
		return redirect("/booking")
	return render (request,'eventForm3.html')

def event4(request):
	if request.method =="POST":
		event = request.POST.get('event')
		eventaddress = request.POST.get('eventaddress')
		dtime = request.POST.get('dtime')
		full_name = request.POST.get('full_name')
		email = request.POST.get('email')
		emailowner = request.POST.get('emailowner')
		mobile_number = request.POST.get('mobile_number')
		date = request.POST.get('date')
		time = request.POST.get('time')
		even = Event(email=email,emailowner=emailowner,mobile_number=mobile_number,full_name=full_name,eventaddress=eventaddress,event=event,date=date,time=time,dtime=dtime)
		even.save()
		messages.info(request, event)
		current_site = get_current_site(request)
		emailsub = "Event Booking Successfull"
		emailbody = render_to_string('mailsendtourself.html',{'eventaddress': eventaddress,
'domain': current_site.domain,
'name': full_name,
'event': event,
'dtime':dtime
})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [email]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
		emailsub = "User book the event"
		emailbody = render_to_string('mailsendtoOther.html',{'domain': current_site.domain,
'event': event,
'name': full_name,
'mobile': mobile_number, 
'email':email,
'datetime':date})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [emailowner]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
	
		return redirect("/booking")
	return render (request,'eventForm4.html')
def event5(request):
	if request.method =="POST":
		event = request.POST.get('event')
		eventaddress = request.POST.get('eventaddress')
		dtime = request.POST.get('dtime')
		full_name = request.POST.get('full_name')
		email = request.POST.get('email')
		emailowner = request.POST.get('emailowner')
		mobile_number = request.POST.get('mobile_number')
		date = request.POST.get('date')
		time = request.POST.get('time')
		even = Event(email=email,emailowner=emailowner,mobile_number=mobile_number,full_name=full_name,eventaddress=eventaddress,event=event,date=date,time=time,dtime=dtime)
		even.save()
		messages.info(request, event)
		current_site = get_current_site(request)
		emailsub = "Event Booking Successfull"
		emailbody = render_to_string('mailsendtourself.html',{'eventaddress': eventaddress,
'domain': current_site.domain,
'name': full_name,
'event': event,
'dtime':dtime
})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [email]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
		emailsub = "User book the event"
		emailbody = render_to_string('mailsendtoOther.html',{'domain': current_site.domain,
'event': event,
'name': full_name,
'mobile': mobile_number, 
'email':email,
'datetime':date})
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [emailowner]
		email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
		email.fail_silently=True
		email.send()
	
		return redirect("/booking")
	return render (request,'eventForm5.html')


def booking(request):
	if request.method =="POST":
		email = request.POST.get('email')
		events = Event.objects.filter(email=email).all()
		return render (request,'booking2.html', {'events':events})
	return render (request,'booking.html')

