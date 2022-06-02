from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class CreateUserForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.TextInput()
    last_name=forms.TextInput()

    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2') 

class UserType(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('is_employer')
 
#this class creates a from that is used to update nanny user profile.




class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('username','email') 
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['phone_number','state','city','religion','education','ethinicity','date_of_birth','image']
            
