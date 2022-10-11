from django.shortcuts import redirect, render
from django.contrib import messages
from geopy.geocoders import Nominatim
from mapeventApp.models import AddEvent
from django import forms
import geocoder
from django.core.exceptions import ValidationError
import datetime
from ckeditor.widgets import CKEditorWidget

class AddEventForm(forms.ModelForm):
		
		def __init__(self, *args, **kwargs):
			super(AddEventForm, self).__init__(*args, **kwargs)
			try:
				nomi_geolocator = Nominatim(user_agent="MyApp")
				g = geocoder.ip('me')
				current_lat_lang = g.latlng
				current_location = nomi_geolocator.geocode(current_lat_lang)
				self.fields['eventaddress'].initial = current_location
			except:
				raise ValidationError({'eventaddress':['Please check your internet connection to get your current address ']})
				
			self.fields['location'].required = False
			self.fields['lat'].required = False
			self.fields['lang'].required = False
			self.label_suffix = ''
			
		class Meta:
			
			model = AddEvent
			fields = '__all__'
			date=datetime.date.today()
			
			#if u use __all__ and want to exclude one or two use this method
			#exclude = ('location','lat','lang')
			
			labels ={
			 'event': 'Event',
			 'info':'Event Details',
			  'eventaddress': 'Enter Full Event Address (we try to locate you current address if it is not accurate or want different address please type the correct address)',
			  'fromdate':'Date From',
			  'todate':'Date Till',
			  'fromtime':'Time Form',
			  'totime':'Time Till',
			  'icon':'Choose an icon',
			  'eventermail':'Enter Owner E-mail Id',
			  'city':'Choose an city'
			  }
			widgets = {
			'fromdate':forms.DateInput(attrs={'type':'date','min':date}),
			'todate':forms.DateInput(attrs={'type':'date','min':date}),
			'fromtime':forms.TimeInput(attrs={'type':'time'}),
			'totime':forms.TimeInput(attrs={'type':'time'}),
			'eventermail':forms.EmailInput(attrs={'type':'email'}),
			'eventaddress':forms.Textarea(attrs={'style':'margin-top:40px;border:none;border-bottom:solid green; height:80px;outline:none' }),'info':forms.Textarea(attrs={'style':'height:300px'})
			}

	
		def clean(self):
			try:
				locate = self.cleaned_data['eventaddress']
				geolocator = Nominatim(user_agent="MyApp")
				self.cleaned_data['location'] = geolocator.geocode(locate)
				self.cleaned_data['lang'] = geolocator.geocode(locate).longitude
				self.cleaned_data['lat'] = geolocator.geocode(locate).latitude
			except:
				raise ValidationError({'eventaddress':['Plase enter a valid address, try to enter your full address']})
			fromdate = self.cleaned_data['fromdate']
			todate = self.cleaned_data['todate']
			fromtime = self.cleaned_data['fromtime']
			totime = self.cleaned_data['totime']
			current_date = date=datetime.date.today()
			current_datetime = datetime.datetime.now()
			two_hours_added_to_c_time = current_datetime + datetime.timedelta(hours=2)
			time = two_hours_added_to_c_time.strftime("%H:%M %p")
			if fromdate > todate:
				raise ValidationError({'todate':['Last event date cant be lesser than start date']})
			try : 
				if todate == current_date and fromtime < time:
					pass
			except:
				raise ValidationError({'fromtime':[' As your event end date is set as today, your event start time should be at least 2 hours greater than your current time']})
			if fromtime > totime:
				raise ValidationError({'totime':['Event end time should be greater than start time']})
			
			return self.cleaned_data
		
		