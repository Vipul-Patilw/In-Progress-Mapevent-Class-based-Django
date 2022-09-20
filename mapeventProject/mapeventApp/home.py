from mapeventApp.models import AddEvent,Staff
from django.shortcuts import redirect, render
from django.core import paginator
from django.template.loader import render_to_string
import datetime
from django.http import JsonResponse
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
NEWS_COUNT_PER_PAGE = 9
def map(request):
	
	if request.user.is_anonymous:
			return redirect ("/login")
	date=datetime.date.today()
	maping = AddEvent.objects.filter(todate__gte=date).all().order_by('fromdate').values()
	pagination = paginator.Paginator(maping,2)
	page_number = request.GET.get('page')
	page = int(request.GET.get('page', 1))
	posts = AddEvent.objects.all().order_by('fromdate')
	p = paginator.Paginator(posts,NEWS_COUNT_PER_PAGE)
	try:
		post_page = p.page(page)
	except paginator.EmptyPage:
		post_page = paginator.Page([], page, p)
		
	if  not is_ajax(request):
		context = {
            'posts': post_page,
        }
		return render(request,
                      'map.html',
                      context)
	
	else:
		content = ''
		for post in post_page:
			content += render_to_string('list-events.html',
                                        {'post': post},
                                        request=request)
		return JsonResponse({
            "content": content,
            "end_pagination": True if page >= p.num_pages else False,
        })
	

	
	#if request.method =="POST":
#	if 'satelite' in request.POST:
#		style_map= request.POST.get('satelite')
#	if 'street' in request.POST:
#		style_map= request.POST.get('street')
#	if 'satelite' not in request.POST and 'street' not in request.POST:
#		style_map= "streets-v11"
	maping1 = {'mapings':maping,'paging':paging}#'style_map':style_map}
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
			
	
	return render (request,'map.html',maping1,)

def eventdetail(request,event_id):
			eventsinfo = AddEvent.objects.filter(id= event_id).all()
			return render(request,'eventdetail.html',{'eventinfo':eventsinfo})

