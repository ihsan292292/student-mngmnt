from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app.models import CustumUser
from django.contrib.auth.decorators import login_required


def INDEX(request):
    return render(request,'index.html')

def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')

def dologin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'))
        if user!= None:
                login(request,user)
                user_type = user.user_type
                if user_type == '1':
                    return redirect('hod_home')
                elif user_type == '2':
                    return redirect('staff_home')
                elif user_type == '3':
                    return redirect('student_home')
                else:
                    messages.error(request,"Email or Password are Invalid")
                    return redirect('login')
        else:
                messages.error(request,"Email or Password are Invalid")
                return redirect('login')

def dologout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def PROFILE(request):
    user = CustumUser.objects.get(id = request.user.id)
    

    context = {
        "user":user
    }
    return render(request,'profile.html')


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #email = request.POST.get('email')
        #username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            custumuser = CustumUser.objects.get(id = request.user.id)

            custumuser.first_name = first_name
            custumuser.last_name = last_name
            custumuser.profile_pic = profile_pic

            if password != None or password != "":
                custumuser.set_password(password)

            if profile_pic != None or profile_pic != "":
                custumuser.profile_pic = profile_pic 
            custumuser.save()
            messages.success(request,'Your profile updated successfully !')
            return redirect('profile')
        except:
            messages.error(request,'Failed to update your profile !')
    return render(request,'profile.html')
    