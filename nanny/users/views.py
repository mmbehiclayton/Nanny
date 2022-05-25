
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CreateUserForm, NannyProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='user_login')
def profile(request):
    return render(request, 'users/profile.html')


@login_required(login_url='user_login')
def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        user_update_form = NannyProfileUpdateForm(request.POST, request.FILES, instance=request.user.nannyprofile)
        if user_form.is_valid() and user_update_form.is_valid():
            user_form.save()
            user_update_form.save()
            return redirect('user_profile')
    else:
        user_update_form=NannyProfileUpdateForm(instance=request.user.nannyprofile)
        user_form=UserUpdateForm(instance=request.user)
    context={
        'user_form': user_form,
        'user_update_form': user_update_form,
        
    }    
    return render(request, 'users/profile_update.html', context)
