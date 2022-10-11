from quopri import decodestring
from mapeventApp.models import UserRegistration
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from mapeventProject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.core.mail import EmailMessage
from django import forms
import datetime
from django.core.exceptions import ValidationError
class UserCreateForm(forms.ModelForm):

	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'type':'password'}))
	confirm_password = forms.CharField(label=' Re-enter Password',widget=forms.PasswordInput(attrs={'type':'password'}))
	access =(('staff_access','Staff Access'),('admin_access','Admin Access'))
	access = forms.ChoiceField(label="Request For",choices=access)
	
	def __init__(self, *args, **kwargs):
			super(UserCreateForm, self).__init__(*args, **kwargs)
			self.fields['access'].required = False

	class Meta:
		model = UserRegistration
		date = datetime.date.today()
		fields = '__all__'
		labels = {
		'first_name': 'First Name',
		
		'last_name':'Last Name',
		
		'mobile_number':'Mobile Number',
		
		'username':'Username',
			
		'email':'Email',
		
		'gender':'Gender',
	
		'birthdate':'Birthdate'
	}
		widgets = {
				'mobile_number':forms.TextInput(attrs={'type':'tel','maxlength':10}),
				'email':forms.EmailInput(attrs={'type':'email'}),
				'password':forms.PasswordInput(attrs={'type':'password'}),
				'birthdate':forms.DateInput(attrs={'type':'date','max':date}),
				'profile_pic':forms.FileInput(attrs={'id':"file" , 'onchange':"loadFile(event)", 'style':"display: none"})}
	def clean(self):
		username= self.cleaned_data['username']
		mobile_number= self.cleaned_data['mobile_number']
		email = self.cleaned_data['email']
		password= self.cleaned_data['password']
		password2 = self.cleaned_data['confirm_password']
		
		if User.objects.filter(email=email):
						raise ValidationError({'email':"this email address already registered with us try different email address"})
			
						
		if User.objects.filter(username=username):
						raise ValidationError({'username':"this username is already exist try another"})
					
		if len(mobile_number) != 10:
				raise ValidationError({'mobile_number':"please enter a valid 10 digit number"})
				
		if len(password)>=6 and re.search(r"[A-Z]",password) and re.search(r"[a-z]",password) and re.search(r"[@_!#$%^&*()?/}{~:]",password)and re.search(r"[0-9]",password):
				pass
				
		else:
				raise ValidationError({'password':"password should be at least 6 character long. contain both uppercase and lowercase character, at least one alpha numeric and one special charecter  (eg:Test@123)"})
				
		if password != password2:
				raise ValidationError({'confirm_password':"confirm password doesn't matched with the password"})
				
	
			#confirmation email
#		current_site = get_current_site(request)
#		email_sub2 = 'Activate your MCCIA Account'
#		message2 = render_to_string('email_confirmation.html',{
#				'fname': first_name,
#				'lname': last_name, 
#				'domain': current_site.domain,
#				'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
#				'token': generate_token.make_token(myuser)
#				})
#		email = EmailMessage(
#				email_sub2,
#				message2,
#				settings.EMAIL_HOST_USER,
#				[email],
#				)
#			
#		email.fail_silently= True
#		email.send()	

#	try:

#	except:
#		messages.error(request,"since google disabled the smpt from 30may2022 we are not able to send mail.So you don't need confirmation link we activate your account you can login now")
#		return redirect('/gotologin')
