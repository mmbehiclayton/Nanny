
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CreateUserForm, NannyProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method=='POST':
        signup_form= CreateUserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('dashboard-index')
    else:
        signup_form= CreateUserForm()  
    #contexts
    context={
        'signup_form':signup_form
        }
        
    
    return render(request, 'users/signup.html',context)

@login_required
def profile_update(request):
    if request.method=='POST':
        user_update_form=NannyProfileUpdateForm(request.POST, request.FILES)
        if user_update_form.is_valid():
            user_update_form.save()
            return redirect('dashboard-index')
    else:
        user_update_form=NannyProfileUpdateForm()
    
    #contexts
    context={
        'user_update_form':user_update_form
    }    
    return render(request, 'users/UpdateProfile.html', context)
