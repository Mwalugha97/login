from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Msafiri, MsafiriCategory, MsafiriDetails
from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages import get_messages
from django.contrib import messages
from .forms import UserForm

def single_slug(request, single_slug):
	categories = [c.category_slug for c in MsafiriCategory.objects.all()]
	if single_slug in categories:
		matching_details = MsafiriDetails.objects.filter(msafiri_category__category_slug=single_slug)
		
		details_urls = {}
		for m in matching_details.all():
			msafiris = Msafiri.objects.filter(msafiri_details__msafiri_details=m.msafiri_details).earliest("msafiri_time")
			details_urls[m] = msafiris.msafiri_slug

		return render(request,
					  "main/category.html",{"msafiris": details_urls})

	msafiris = [m.msafiri_slug for m in Msafiri.objects.all()]
	if single_slug in msafiris:
		this_msafiris = Msafiri.objects.get(msafiri_slug = single_slug)
		return render(request,
					  "main/msafiri.html",
					  {"msafiri":this_msafiris})

	return HttpResponse(messages.INFO,'{single_slug} doesnt correspond to anything.')



# Create your views here.
def homepage(request):
	return render(request=request,
				  template_name="main/categories.html",context={"categories": MsafiriCategory.objects.all})


def register(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, messages.INFO,'New account created {username}')
			login(request, user)
			messages.info(request, messages.INFO,'Login Successful {username}')
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, messages.INFO,'{msg}: {form.error_messages[msg]}') 


	form = UserForm
	return render(request,
				  "main/register.html",
				  context={"form" :form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged Out Successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, messages.INFO,'Login Successful {username}')
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")


	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})