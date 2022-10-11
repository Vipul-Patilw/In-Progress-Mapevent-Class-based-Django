from django.views.generic.edit import CreateView
from mapeventApp.forms import  AddEventForm
from mapeventApp.models import  AddEvent
from django.contrib.auth.mixins import  LoginRequiredMixin
class CreateEvent(LoginRequiredMixin,CreateView):
		model = AddEvent
		template_name = 'addevent.html'
		form_class = AddEventForm
		success_url = '/map'
		def form_valid(self, form):
			form.clean()
			return super(CreateEvent, self).form_valid(form)