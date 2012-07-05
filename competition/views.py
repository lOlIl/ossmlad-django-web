from django.http import HttpResponse

def home(request):
	return HttpResponse("HOME page")

def index(request):
	return HttpResponse("Hello Event list")

def detail(request, event_id):
	return HttpResponse("Hello Event detail %s" % event_id)
