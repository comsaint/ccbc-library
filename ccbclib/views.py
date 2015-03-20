from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to CCBC Library!")

def about(request):
    context_dict = {}
    return render(request, 'ccbc-library/about.html', context_dict)

def home(request):
    context_dict = {}
    return render(request, 'ccbc-library/home.html', context_dict)

def borrow(request):
    context_dict = {}
    return render(request, 'ccbc-library/borrow.html', context_dict)