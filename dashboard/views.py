from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request,'dashboard/home.html')

@login_required
def about(request):
    return render(request,'dashboard/about.html')

@login_required
def help(request):
    return render(request,'dashboard/help.html')

@login_required
def tips(request):
    return render(request,'dashboard/tips.html')


