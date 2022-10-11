from django.views.generic.edit import DeleteView
from mapeventApp.models import  AddEvent
from django.contrib.auth.mixins import  LoginRequiredMixin
class DeleteEvent(LoginRequiredMixin,DeleteView):
		model = AddEvent
		template_name = 'delete_event.html'
		success_url = '/eventeditpage'