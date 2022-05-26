from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import NannyProfile

# Create your views here.

def index(request):
     data=User.objects.all()
     # ndata=NannyProfile.objects.all()
     context={
          'data':data,
          # 'ndata':ndata
     }
     return render(request, 'dashboard/index.html', context)


@login_required(login_url='user_login')
def dashboard(request):
     return render(request, 'dashboard/dashboard.html')