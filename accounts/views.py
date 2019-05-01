from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# from django.views.generic import view
from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth import authenticate, login
# from .forms import UserForm
from django.contrib.auth import authenticate, login
from .models import Events



def index(request):
	all_events = Events.objects.all()
	html = ''
	for events in all_events:
		url = '/index/' + str(events.id) + '/'
		html += '<a href ="' + url + '">'+ events.event_name+'</a><br>'
	return HttpResponse(html)
	
def contestants(request):
	all_constestants = Contestant.objects.all()
	html = ''
	for constestants in all_constestants:
		url = '/index/' + str(events.id) + '/'
		html += '<a href ="' + url + '">'+ events.event_name+'</a><br>'



	
def detail(request, events_id):
	return render(request,'details for events'+ str(events_id))



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



	


