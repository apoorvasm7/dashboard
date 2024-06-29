from django.shortcuts import render, redirect
from django import forms
from .models import *
from .forms import UserImage
from .models.user import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def doc_sign(request):

    return render(request, 'sign.html')


def signupdetails(request):
    pic = request.FILES['image']
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    uname = request.POST.get('uname')
    email = request.POST.get('email')
    usertype = request.POST.get('usertype')
    address = ''
    space=" "
    address += request.POST.get('add1')
    address += space
    address += request.POST.get('city')
    address += space
    address += request.POST.get('state')
    address += space
    address += request.POST.get('pincode')
    password = request.POST.get('passw')
    cpassword = request.POST.get('con_passw')
    err_msg = None
    
    if (password != cpassword):
        err_msg = "Enter correct password in both password fields"
    if err_msg == None:
        
        newuser = User(
            fname=fname,
            lname=lname,
            photo=pic,
            uname=uname,
            email=email,
            password=password,
            address=address,
            usertype=usertype
        )
        newuser.password = make_password(newuser.password)
        newuser.register()
        return render(request, 'login.html')
    else:
        return render(request, 'sign.html', {'err_msg': err_msg})

def login(request):
    if request.POST:
        uname=request.POST.get('login')
        passw=request.POST.get('passw')
        details = User.uname_login(uname)
        err_msg = None
        if details:
            flag = check_password(passw, details.password)
            print(passw)
            print(details.password)
            print(flag)
            if flag:
                request.session['user_id'] = details.id
                request.session['user_name'] = details.uname
                request.session['user_email'] = details.email
                if details.usertype=="patient":
                    return redirect('patientpage')
                if details.usertype=="doctor":
                    return redirect('doctorpage')
            else:
                err_msg = "Incorrect Password !!!"
                return render(request, 'login.html', {'err_msg': err_msg})
        else:
            err_msg = "Invalid Username !!!"
            return render(request, 'login.html', {'err_msg': err_msg})
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def patient(request):
    ids = int(request.session.get('user_id'))
    result = User.get_user_by_id(ids)        
    return render(request, 'patientpage.html', {'ress': result})

def doctor(request):
    ids = request.session.get('user_id')
    result = list(User.get_user_by_id(ids))
    return render(request, 'doctorpage.html', {'ress': result})