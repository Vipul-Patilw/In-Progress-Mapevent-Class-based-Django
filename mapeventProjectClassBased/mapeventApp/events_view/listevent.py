from django.views.generic import ListView
from mapeventApp.models import  AddEvent
from django.contrib.auth.mixins import  LoginRequiredMixin
import datetime

class ListEventHome(LoginRequiredMixin,ListView):
    template_name = 'map.html'
    context_object_name = 'event_list'
    date=datetime.date.today()
    queryset  = AddEvent.objects.filter(todate__gte=date).all().order_by('fromdate')
    
class ListEventForEditDelete(LoginRequiredMixin,ListView):
    template_name = 'list_event_for_edit.html'
    context_object_name = 'event_list'
    date=datetime.date.today()
    queryset  = AddEvent.objects.filter(todate__gte=date).all().order_by('fromdate')
 