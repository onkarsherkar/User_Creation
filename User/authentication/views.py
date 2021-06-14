from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def hello(request):
   return HttpResponse('Hello Django')

def home(request):
   return render(request,'master.html',{})

def signup(request):
   form = CreateUserForm()
   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request,'Account created Successfully')
         return redirect(login_user)
   
   return render(request,'signup.html',{'form':form})

def login_user(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')


      user = authenticate(request,username=username,password=password)

      if user is not None:
         print('yes')
         login(request,user)
         #return HttpResponse('Welcome user')
         return redirect(home)
      else:
         messages.info(request,'Invalid Username or Password')
         return render(request,'login.html',{})

   return render(request,'login.html',{})

def logout_user(request):
   logout(request)
   return redirect(home)
