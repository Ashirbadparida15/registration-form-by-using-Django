from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
       

    if request.method=='POST':
        # user_type = request.POST.get('user')
        fname=request. POST.get('first_name')
        lname=request.POST.get('last_name')
        uname=request.POST.get('username')
        email=request.POST.get('email_id')
        add=request.POST.get('address_line-1')
        city=request.POST.get('city')
        state=request.POST.get('State')   
        pin=request.POST.get('Pincode')
        pic=request.POST.get('Profile_Picture')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')
        if pass1 != pass2:
            return HttpResponse("your password and confirm password are not same")
       
       
        else:
            hashed_pass=make_password(pass1)
            my_user=User.objects.create_user(username=uname,password=hashed_pass,first_name=fname,email=email)
            my_user.save()
            return redirect('login')

        #print(fname,lname,uname,email,pass1,pass2,add,city,state,pin,pic)

        
    return render(request,'signup.html')

def LoginPage(request):
     if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('home')
            # return HttpResponse ("Username or Password is incorrect!!!")

     return render(request,'login.html')