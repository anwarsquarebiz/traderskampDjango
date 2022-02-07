from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# Index page
def index(request):
    return HttpResponse("Hello, World this is my new app")

def dashboard(request):
    return HttpResponse('Dashboard')

def signIn(request):
    return HttpResponse('Sign In')

def signOut(request):
    return HttpResponse('Sign Out')

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponse('Contact Us')

def register(request):
    return HttpResponse('Register')

def resetpassword(request):
    return HttpResponse('Reset Password')
