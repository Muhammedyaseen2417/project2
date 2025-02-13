from django.shortcuts import render,redirect
from . models import Event
from   .forms import BookingForm

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_eve)

def bookings(request):
    if request.method=='POST':
        form=BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('booking_')
     
    form=BookingForm()
    dict_form={
        'form':form
    }

    return render(request,'bookings.html',dict_form)

def contact(request):
    return render(request,'contact.html')