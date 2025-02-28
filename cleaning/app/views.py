from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User


# Create your views here.
def shp_login(req):
    if 'cleaning' in req.session:
        return redirect(admin_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['cleaning']=uname   #create session
                return redirect(admin_home)
            else:
                login(req,data)
                req.session['user']=uname   #create session
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(shp_login)
    
    else:
        return render(req,'login.html')
    
def shp_login1(req):
    if 'cleaning' in req.session:
        return redirect(admin_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['cleaning']=uname   #create session
                return redirect(admin_home)
            else:
                login(req,data)
                req.session['user']=uname   #create session
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(shp_login)
    
    else:
        return render(req,'login.html')
    




def shp_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(shp_login)






def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(shp_login)
        except:
            messages.warning(req,'User already exists.')
            return redirect(register)
    else:
        return render(req,'user/register.html')
    

    # -------------------------------------admin-------------------------------------

def admin_home(request):
    return render(request, 'admin/home.html')





def admin_bookings(request):
    # Get all appointments from the database
    appointments = Appointment.objects.all().order_by('-date')  # Orders by date, with the most recent first
    return render(request, 'admin/bookings.html', {'appointments': appointments})


def delete_bookings(request, appointment_id):
    # Fetch the appointment object or return 404 if not found
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Delete the appointment from the database
    if request.method == "POST":
        appointment.delete()
        return redirect('admin_bookings')  # 

    # If the request method isn't POST, raise 404 (not allowed here)
    raise Http404("Invalid request method")

    # -----------------------------------------user--------------------------------------





def user_home(request):
    return render(request, 'user/home.html')


# Book Appointment Page
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def booking(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        service = request.POST['service']
        date = request.POST['date']

        # Check if the selected time is already booked
        if Appointment.objects.filter(date=date).exists():
            messages.error(request, 'The selected time slot is already booked. Please choose another time.')
            return redirect('booking')  # Redirect back to the booking form with the error

        # If the time is available, create the appointment
        appointment = Appointment.objects.create(
            user=request.user,  # Associate the appointment with the logged-in user
            name=name, 
            email=email, 
            service=service, 
            date=date
        )
        messages.success(request, 'Your appointment has been booked successfully!')
        return redirect('booking_success')  # Redirect to appointment success page or another page as required

    return render(request, 'user/booking.html')



def booking_success(request):
    return render(request, 'user/booking_success.html')

def view_bookings(request):
    # Get the appointments for the current logged-in user
    appointments = Appointment.objects.filter(user=request.user)

    # Render the template and pass the appointments to it
    return render(request, 'user/view_bookings.html', {'appointments': appointments})
