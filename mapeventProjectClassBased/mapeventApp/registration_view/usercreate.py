from django.views.generic.edit import CreateView
from django.contrib.messages.views import  SuccessMessageMixin
from mapeventApp.forms import UserCreateForm
from mapeventApp.models import  UserRegistration
from django.contrib.auth.models import User

class UserCreate(CreateView,SuccessMessageMixin):

		model = UserRegistration
		template_name = 'registration/user_registration.html'
		form_class = UserCreateForm
		success_message = "Welcome<strong> %,<%(first _name) %(last_name) </strong> Your account is created sucsessfully."
		success_url = 'accounts/login'
		def form_valid(self, form):
			username= form.cleaned_data['username']
			first_name= form.cleaned_data['first_name']
			last_name= form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password= form.cleaned_data['password']
			myuser = User.objects.create_user(username,email,password)
			myuser.first_name = first_name
			myuser.last_name = last_name
			#myuser.is_active = False
			myuser.save()
			return super(UserCreate, self).form_valid(form)