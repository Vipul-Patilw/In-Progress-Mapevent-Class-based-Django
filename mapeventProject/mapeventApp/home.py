from mapeventApp.models import AddEvent,Staff
from django.shortcuts import redirect, render
from django.core.paginator import  Paginator
import datetime
def map(request):
	if request.user.is_anonymous:
			return redirect ("/login")
	date=datetime.date.today()
	maping = AddEvent.objects.filter(todate__gte=date).all().order_by('fromdate').values()
	staff = Staff.objects.all()
	pagination = Paginator(maping,2)
	page_number = request.GET.get('page')
	
	try:
	   paging = pagination.get_page(page_number)
	except PageNotAnInteger:
	   paging = pagination.get_page(1)
	except EmptyPage:
		paging = pagination.get_page(pagination.num_pages)
	maping1 = {'mapings':maping,'staff':staff,'paging':paging}
	
	#if request.method =="POST":
	if 'search' in request.POST:
				
					search= request.POST.get('search')
					events = AddEvent.objects.filter(event__icontains = search).all()
					location = AddEvent.objects.filter(location__icontains = search).all()
					return render(request,'searchDetail.html',{'events':events,'searches':search,'locations':location})
	if 'lat' in request.POST:
					lang = request.POST.get('lang')
					lat = request.POST.get('lat')
					return  render(request,'map.html',{'lat':lat,'lang':lang,'mapings':maping,'paging':paging})
	if 'active_event' in request.POST:
				active_event = request.POST.get('active_event')
				eventsbook = AddEvent.objects.filter(id= active_event).all()
				return render(request,'eventForm1.html',{'bookevents':eventsbook})
	if 'event_id' in request.POST:
			event_id = request.POST.get('event_id')
			eventsinfo = AddEvent.objects.filter(id= event_id).all()
			return render(request,'eventdetail.html',{'eventinfo':eventsinfo})
			
	
	return render (request,'map.html',maping1)
