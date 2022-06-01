
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Login(models.Model):
	
	first_name = models.CharField(max_length=122)
	
	last_name = models.CharField(max_length=122)
	
	mobile_number= models.CharField(max_length=122)
	
	username= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)

	password= models.CharField(max_length=122)
	
	gender = models.CharField(max_length=122)

	birthdate = models.DateField()
	
	
	
	def __str__(self):
		return self.first_name 
	
class Sign(models.Model):
	username  = models.CharField(max_length=122)
	Loginpassword = models.CharField(max_length=122)
	def __str__(self):
		return self.name
		
		
class SendMoney(models.Model):
		add = datetime.now
		full_name = models.CharField(max_length=122)
		email = models.CharField(max_length=122)
		emailowner= models.CharField(max_length=122)
		mobile_number= models.CharField(max_length=122)
		address= models.CharField(max_length=122)

		def __str__(self):
			return self.amount


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
		
	
class AddEvent(models.Model):
		event = models.CharField(max_length=122)
		info = models.CharField(max_length=122)
		lang = models.FloatField()
		lat = models.FloatField()
			
class ForgotPassword(models.Model):
	email = models.CharField(max_length=222)