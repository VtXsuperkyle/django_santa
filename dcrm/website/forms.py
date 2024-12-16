from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import santa_user
from django import forms
from django.forms.widgets import PasswordInput, TextInput




#register or create a user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = santa_user
        fields = ['username','password1','password2']


#login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#add record
class CreationRecordForm(forms.ModelForm):
    class Meta:
        model = santa_user
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city']

class UpdateRecordForm(forms.ModelForm):
        class Meta:
             model = santa_user
             fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city']
class reindeer_booking(forms.ModelForm):
     
    class Meta:
        model = reindeerbooking

        fields = ['ride_booking_date_arrive', 'ride_booking_date_leave', 'ride_booking_adults',
        'ride_booking_children', 'ride_total_cost']
        labels={
             "ride_booking_date_arrive": 'day you wish to arrive'
        }
        widgets = {
             'ride_booking_date_arrive': forms.DateInput(attrs={'type': 'date'}),
             'ride_booking_date_leave': forms.DateInput(attrs={'type': 'date'}),
             'ride_total_cost': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args,**kwargs)