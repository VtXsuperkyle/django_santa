from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm, CreationRecordForm, UpdateRecordForm, reindeer_booking_form

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import santa_user, reindeerbooking
#from.models import Record




def home(request):
    return render(request, 'website/index.html')

#register a user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')

    context = {'form': form}

    return render(request, 'website/register.html', context=context)

#login a user
def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request,data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'login_form':form}
    return render(request,'website/my-login.html', context=context)

#logout user
def logout(request):
    auth.logout(request)
    return redirect("my-login")


@login_required(login_url='my-login')
def create_record(request):

    form = CreationRecordForm()
    if request.method == "POST":
        form = CreationRecordForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    {'create_form': form}
    return render(request, 'website/create-record.html', context=context)


@login_required(login_url='my-login')
def update_record(request):

    #record = Record.objects.get(id=pk)
    form= UpdateRecordForm(instance=record)

    if request.method =="POST":
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    context = {'update_form': form}
    return render(request, 'website/update-record.html')


@login_required(login_url='my-login')
def singular_record(request, pk):
    on_Record = Record.objects.get(id=pk)
    context = {'record':one_record}
    return render(request, 'webiste/view-record.html', context=context)


@login_required(login_url='my-login')
def delete_record(request,pk):
    record = Record.objects.get(id=pk)
    record.delete()

    return redirect("dashboard")

#dashboard
@login_required(login_url='my-login')
def dashboard(request):

    my_ride_bookings = reindeerbooking.objects.filter(ride_user_id = request.user.id)
    context = {'ride_records': my_ride_bookings,}

    return render(request, 'website/dashboard.html', context=context)


@login_required(login_url='my-login')
def santa(request):

    form = reindeer_booking_form()

    if request.method =="POST":
        updated_request = request.POST.copy()
        updated_request.update({'ride_user_id_id': request.user})

        form = reindeer_booking_form()

        if form.is_valid():
            obj = form.save(commit=False)


            arrive = obj.ride_booking_date_arrive
            depart = obj.ride_booking_date_leave
            result = depart - arrive
            print("Number of days: ", result.days)


            ride_total_cost = int(obj.ride_booking_adults) * 65 \
                                    * int(obj.ride_booking_children) * 15
            
            ride_total_cost *= int(result.days)

            obj.ride_total_cost = ride_total_cost
            obj.ride_user_id = request.user

            obj.save()

            return redirect('')
        else:
            print("there was a problem with the form")
            return redirect('santa')
    
    context = {'form': form}

    return render(request, 'website/santa.html', context=context)