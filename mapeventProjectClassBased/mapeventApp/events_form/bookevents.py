#!/usr/bin/python
# -*- coding: utf-8 -*-
from mapeventApp.models import Event,AddEvent
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from mapeventProject import settings
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from django import forms
import datetime
class BookEventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = '__all__'
		date=datetime.date.today()
		labels ={
			 'event': 'Event',
			 'eventaddress':'Event Address',
			  'dtime': 'Date And Time Of Event',
			  'full_name':'Full Name',
			  'email':'Email',
			  'mobile_number':'Mobile Number',
			  }
		widgets = {
			'date':forms.DateInput(attrs={'type':'date','min':date}),
			'time':forms.TimeInput(attrs={'type':'time'}),
			'email':forms.EmailInput(attrs={'type':'email'}),
			'eventaddress':forms.Textarea(attrs={'style':'margin-top:40px;border:none;border-bottom:solid green; height:80px;outline:none' })
			}
	      
		
	def clean (self):
	     current_date = datetime.date.today()
		 event = self.cleaned_data['event']
		 email = self.cleaned_data['email']
		 emailowner = self.cleaned_data['emailowner']
		 mobile_number = self.cleaned_data['mobile_number']
		 date = self.cleaned_data['date']
		 time = self.cleaned_data['time']
		 booker = AddEvent.objects.get(event=event)
		 current_datetime = datetime.datetime.now()
		 one_hours_added_to_c_time = current_datetime + datetime.timedelta(hours=1)
		 current_time = one_hours_added_to_c_time.strftime("%H:%M %p")
	  
	  if date == current_date and time < current_time:
	     	raise ValidationError({'time':['If You are trying to book event for today the time should be great than 1hours of current time']})
	     

           
                                 #	     messages.info(request, event)
#           	     current_site = get_current_site(request)
#           	     emailsub = 'Event Booking Successfull'
#           	     emailbody = render_to_string('mailsendtourself.html', {
#			            'eventaddress': eventaddress,
#			            'domain': current_site.domain,
#			            'name': full_name,
#			            'event': event,
#			            'dtime': dtime,
#			            })
#           	     from_mail = settings.EMAIL_HOST_USER
#           	     to_mail = [email]
#           	     email = EmailMessage(emailsub, emailbody, from_mail, to_mail)
#           	     email.fail_silently = True
#           	     email.send()
#           	     emailsub = 'User book the event'
#           	     emailbody = render_to_string('mailsendtoOther.html', {
#			            'domain': current_site.domain,
#			            'event': event,
#			            'name': full_name,
#			            'mobile': mobile_number,
#			            'email': even.email,
#			            'datetime': date,
#			            })
#           	     from_mail = settings.EMAIL_HOST_USER
#           	     to_mail = [emailowner]
#           	     email = EmailMessage(emailsub, emailbody, from_mail, to_mail)
#           	     email.fail_silently = True
#           	     email.send()
#           	     return redirect('/booking')
#           
#           
#           except:
#           	messages.error(request,"mail has not sent cause Google ban smtp feature from 30may 2022. you can check your bookings from here;")
#           	return redirect('/booking')
#    return render(request, 'eventForm1.html')
#			        