from django.views.generic.edit import CreateView
from django.contrib.messages.views import  SuccessMessageMixin
from mapeventApp.forms import UserCreateForm
from mapeventApp.models import  UserRegistration,Admin,Staff
from django.contrib.auth.models import User

class SuperUserCreate(CreateView,SuccessMessageMixin):

		model = UserRegistration
		template_name = 'registration/user_registration.html'
		form_class = UserCreateForm
		success_message ='''Welcome<strong> %,<%(first _name) %(last_name) </strong> Your account is created request for the has been send to admin if he accept the request you will able to use this account'''
		success_url = 'adminlogin'
		def form_valid(self, form):
			username= form.cleaned_data['username']
			first_name= form.cleaned_data['first_name']
			last_name= form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password= form.cleaned_data['password']
			access = form.cleaned_data['access']
			myuser = User.objects.create_user(username,email,password)
			myuser.first_name = first_name
			myuser.last_name = last_name
			myuser.is_active = False
			myuser.save()
			if access == "staff_access":
				users = Staff(first_name=first_name,username=username, last_name=last_name,email=email)
				users.save()
			if access == "admin_access":
				users = Admin(first_name=first_name,username=username, last_name=last_name,email=email)
				users.save()
			return super(SuperUserCreate, self).form_valid(form)