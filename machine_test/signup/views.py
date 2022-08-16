from django.shortcuts import render,redirect
from signup.models import *
# Create your views here.
def index(request):
    if request.method=="POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        obj=User(f_name=f_name,l_name=l_name,email=email,phone=phone,password=password)
        obj.save()
        return redirect('login')
    else:    
        return render(request,'index.html')

def login(request):
    msg=""
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            data=User.objects.get(email=username,password=password)
            return redirect('home')
        except: 
            msg="invalid "       
    return render(request,'login.html',{"msg":msg})

def home(request):
    return render(request,'home.html')