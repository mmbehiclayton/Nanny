
from django.shortcuts import render, redirect
from .forms import CreateUserForm

# Create your views here.
def signup(request):
    if request.method=='POST':
        signup_form= CreateUserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('Homepage')
    else:
        signup_form= CreateUserForm()    
    return render(request, 'users/signup.html',{'signup_form':signup_form})
