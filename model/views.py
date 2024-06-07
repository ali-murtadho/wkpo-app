from django.shortcuts import render
from . forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def adminIndex(request):
    return render(request, 'admin-index.html')

def dataset(request):
    return render(request, 'data.html')

def result(request):
    return render(request, 'result.html')

def classification(request):
    return render(request, 'klasifikasi.html')

def register(request):
    return render(request, 'register.html')

def excel(request):
    return render(request, 'excel.html')