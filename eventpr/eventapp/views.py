from django.shortcuts import render,redirect
from . models import Event
from   .forms import BookingForm

def index(request):
    return render(request,'user/index.html')

def about(request):
    return render(request,'user/about.html')

def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'user/events.html',dict_eve)

def bookings(request):
    if request.method=='POST':
        form=BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('sucess')
     
    form=BookingForm()
    dict_form={
        'form':form
    }

    return render(request,'user/bookings.html',dict_form)

def contact(request):
    return render(request,'user/contact.html')

def appoiments(request):
    return render(request,'user/mybooking.html')



def sucess(request):
    return render(request,'user/booking_sucess.html')


# admin

def admin_home(request):
    return render(request,'admin/home.html')







from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.


def event_login(req):
    if 'eventpr' in req.session:
        return redirect(admin_home)
    if 'user' in req.session:
        return redirect(index)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['eventpr']=uname   #create session
                return redirect(admin_home)
            else:
                login(req,data)
                req.session['user']=uname   #create session
                return redirect(index)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(event_login)
    
    else:
        return render(req,'login.html')
    




def event_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(event_login)






def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(event_login)
        except:
            messages.warning(req,'User already exists.')
            return redirect(register)
    else:
        return render(req,'user/register.html')