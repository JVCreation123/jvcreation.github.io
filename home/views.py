from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("this is homepage")
    
def about(request):
    # return HttpResponse("this is about page")
     return render(request, 'about.html')
    
def services(request):
    # return HttpResponse("this is services page")
     return render(request, 'services.html')

def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        contact = Contact(name=name, email=email, password=password, phone=phone, date = datetime.today())
        contact.save()
        messages.success(request, 'You are Successfull Registered.')
    return render(request, 'contact.html')