from django.views.generic.edit import UpdateView
from mapeventApp.forms import  AddEventForm
from mapeventApp.models import  AddEvent
from django.contrib.auth.mixins import  LoginRequiredMixin
class UpdateEvent(LoginRequiredMixin,UpdateView):
		model = AddEvent
		template_name = 'addevent.html'
		form_class = AddEventForm
		success_url = '/listevent'
		def form_valid(self, form):
			form.clean()
			return super(UpdateEvent, self).form_valid(form)