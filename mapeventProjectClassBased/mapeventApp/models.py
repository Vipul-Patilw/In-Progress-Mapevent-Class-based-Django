#
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from geopy.geocoders import Nominatim
from django_quill.fields import QuillField
from ckeditor.fields import  RichTextField
from tinymce.models import HTMLField
# Create your models here.
gender=[('','Select Gender'),('male','Male'),('female','Female')]

class UserRegistration(models.Model):
	
	profile_pic = models.ImageField(upload_to= "mapeventApp/images",blank=True)

	first_name = models.CharField(max_length=122)
	
	last_name = models.CharField(max_length=122)
	
	mobile_number= models.CharField(max_length=122)
	
	username= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)
	
	gender = models.CharField(max_length=122,choices=gender)

	birthdate = models.DateField()
	
	
	

	def __str__(self):
		return self.first_name 

class Staff(models.Model):
	
	first_name = models.CharField(max_length=122)
	
	last_name = models.CharField(max_length=122)
	
	username= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)
		
	def __str__(self):
		return self.first_name 
		
class Admin(models.Model):
	
	first_name = models.CharField(max_length=122)
	
	last_name = models.CharField(max_length=122)
	
	username= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)

		
	def __str__(self):
		return self.first_name 



class ChangePassword(models.Model):
		old_password = models.CharField(max_length=122)
		new_password1= models.CharField(max_length=122)
		newpassword2 = models.CharField(max_length=122)


class Event(models.Model):
		event = models.CharField(max_length=122)
		eventaddress = models.TextField()
		dtime = models.CharField(max_length=122)
		full_name = models.CharField(max_length=122)
		email = models.CharField(max_length=122)
		emailowner = models.CharField(max_length=122)
		mobile_number = models.CharField(max_length=122)
		date = models.DateField()
		time = models.TimeField()

		def __str__(self):
			return self.event 
		
class Add(models.Model):
		event = models.CharField(max_length=122)
		box = models.CharField(max_length=122)
		
		def __str__(self):
			return self.event

				
icon_choices= [('','Select Icon'),('bar-15','Bar Icon'),('music-15','Music Icon'),('art-gallery-15','Art Gallary Icon')]

city_choices=[('','Select City'),('mumbai','Mumbai'),('pune','Pune'),('delhi','Delhi'),('kolkatta','Kolkatta')]
				
class AddEvent(models.Model):
		event = models.CharField(max_length=122)
		info = QuillField()
		eventaddress = models.TextField()
		fromdate = models.DateField()
		todate= models.DateField()
		fromtime = models.TimeField()
		totime= models.TimeField()
		icon = models.CharField(max_length=122,choices=icon_choices)
		eventermail = models.CharField(max_length=122)
		city = models.CharField(max_length=122,choices=city_choices)
		location = models.TextField()
		lat = models.CharField(max_length=122)
		lang = models.CharField(max_length=122)	

		def __str__(self):
			return self.city
			
class LocateEvent(models.Model):
		lat = models.CharField(max_length=122)
		lang = models.CharField(max_length=122)			
class ForgotPassword(models.Model):
	email = models.CharField(max_length=222)
