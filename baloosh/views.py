from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from booking import settings

# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        try:
            remember = request.POST['remember-me']
            if remember:
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        except:
            is_private = False
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True

        if user is not None:
            login(request, user)
            messages.success(request, "LOGGED IN SUCCESSFULLY!")
        else:
            messages.error(request, "BAD CREDENTIALS")
            return redirect('/')

    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')

def accomodation(request):
    return render(request, 'accomodation.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def signout(request):
    logout(request)
    messages.success(request, "LOGGED OUT SUCCESSFULLY!")
    return redirect('/')