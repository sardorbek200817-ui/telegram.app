from django.shortcuts import render , redirect
from .models import User_profile
from django.contrib.auth import authenticate
# Create your views here.


def login_user(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            return render(request, "telegram/home.html")
        else:
            error_message = "Email yoki parol xato"
    return render(request, "telegram/login.html", {"error_message": error_message})
        




def register(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    try:
        User_profile.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email=email,
            password=password,
        )
        return render(request , "telegram/login.html")
    
    except Exception:
        return render(request, "telegram/register.html")


    

    
    