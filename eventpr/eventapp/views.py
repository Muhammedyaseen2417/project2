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
            return redirect('view_bookings')
     
    form=BookingForm()
    dict_form={
        'form':form
    }

    return render(request,'user/bookings.html',dict_form)

def contact(request):
    return render(request,'user/contact.html')

def view_bookings(request):
    return render(request,'user/mybooking.html')



