from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Msafiri
from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import get_messages
from django.contrib import messages


# Create your views here.
def homepage(request):
	return render(request=request,template_name="main/home.html",context={"msafiri": Msafiri.objects.all})


def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, message.INFO,'New account created {username}')
			login(request, user)
			messages.info(request, message.INFO,'Login Successful {username}')
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, message.INFO,'{msg}: {form.error_messages[msg]}') 


	form = UserCreationForm
	return render(request,
				  "main/register.html",
				  context={"form" :form})