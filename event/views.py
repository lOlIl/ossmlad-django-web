from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from event.forms import LoginForm, RegistrationForm
from django.utils import simplejson
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from event.models import Member

def home(request):
	return HttpResponse("HOME page")

def index(request):
	return render_to_response("index.html", {})

def detail(request, event_id):
	id = request.GET.get('id', None)
	tel = request.GET.get('tel', None)
	sms = request.GET.get('sms', None)

	if id is not None and tel is not None and sms is not None:
		smss = list()
		# loaded from DB
		for i in range(1,5):
			smss.append({'text':sms})	

		data = dict(id=id, tel=tel, sms=smss)

		resp = simplejson.dumps({'data':data})
		return HttpResponse(resp, mimetype='application/json')
	else:
		return HttpResponse("Hello Event detail %s" % event_id)

@csrf_protect
def registration(request):
	form = RegistrationForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		email = form.cleaned_data['email']
		tel = form.cleaned_data['tel']

		user = User.objects.create_user(username, email, password)
		user.save()

		member = Member(user=user, tel=tel)
		member.save()

		return HttpResponse("Thank You %s" % user)
	
	return render_to_response(
			'registration.html', 
			{ 'form':form }, 
			context_instance=RequestContext(request))

@csrf_protect
def login_user(request):
	state = 'Please login below'
	form = LoginForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You are successfully logged in!"
			else:
				state = "Your account is not activated."
		else:
			state = "Wrong crendetial for username/password"
	
	return render_to_response(
			'login.html', 
			{ 'state':state, 'form':form }, 
			context_instance=RequestContext(request))
