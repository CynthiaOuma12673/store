from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
            
    else:
        form = UserRegistrationForm()
    return render(request,"registration/signup.html",{'form':form})

