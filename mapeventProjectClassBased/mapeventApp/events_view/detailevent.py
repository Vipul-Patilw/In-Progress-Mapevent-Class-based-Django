from django.views.generic import DetailView
from mapeventApp.models import  AddEvent
from django.contrib.auth.mixins import  LoginRequiredMixin

class DetailEvent(LoginRequiredMixin,DetailView):
    template_name = 'eventdetail.html'
    context_object_name = 'event_detail'
    model  = AddEvent
