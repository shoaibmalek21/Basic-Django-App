from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


def home(request):
	return render(request,'base.html')
