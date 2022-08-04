from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from baloosh.models import Bookings, Contact
from django.contrib.auth.models import User
from booking import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def home_login(request):
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

def home_register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        country = request.POST['country']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please use some other username, thank you.")
            return redirect('/')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('/')

        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')

        if len(contact)<10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('/')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.contact = contact
        myuser.country = country
        myuser.is_active = True
        myuser.save()
        messages.success(request, "ACCOUNT CREATED SUCCESSFULLY, PROCEED TO LOGIN")

    return render(request, "home.html")

def userview(request):
    context = {
        'user' : request.user,
        
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def accomodation(request):
    if request.method == 'POST':
        arrivaldates = request.POST['arrivaldates']
        departuredates = request.POST['departuredates']
        adults = request.POST['adults']
        children = request.POST['children']
        noofrooms = request.POST['noofrooms']
        roomtypes = request.POST['roomtypes']

        book = Bookings(arrivaldates = arrivaldates, departuredates = departuredates, adults = adults, children = children, noofrooms = noofrooms, roomtypes = roomtypes, )
        book.save()
        messages.success(request, "HOTEL ROOM HAS BEEN BOOKED")
    return render(request,  'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        new_message = Contact(name = name, email = email, subject = subject, message = message)
        new_message.save()
        messages.success(request, "MESSAGE SENT, THANK YOU FOR CONTACTING PANDA")

    return render(request, 'contact.html')

def signout(request):
    logout(request)
    messages.success(request, "LOGGED OUT SUCCESSFULLY!")
    return redirect('/')