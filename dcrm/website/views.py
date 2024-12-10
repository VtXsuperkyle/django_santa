from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm

def home(request):
    return render(request, 'website/index.html')

#register a user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('')

    context = {'form': form}

    return render(request, 'website/register.html', context=context)