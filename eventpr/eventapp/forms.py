from django import forms
from .models import Booking  # Import the model
class DateInput(forms.DateInput):
    input_type='date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking  # Ensure this is set
        fields = '__all__'  # Or specify the fields explicitly


        widgets={
            'booking_date':DateInput(),
        }


        labels={
            'cus_name':"Enter Your Name",
            'cus_mob' :"Enter Your Mobile Number",
            'cus_addres' :"Enter your address",
            'event_name' :"Event Name",
            
        }
