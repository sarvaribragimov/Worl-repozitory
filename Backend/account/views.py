from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# from .models import Profile
# Create your views here.
def index(request):
    return render(request,'signin.html')

def login(request):
    if request.method == 'POST':
        username =  request.POST['username']
        password =  request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:    
            print('foydalanuvchi yuq')

        user = authenticate(request,username=username,password=password)
    return render(request,'login.html')        