from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm

# Profile
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect(reverse('login'))

# Authentication 

#Register
def registration(request):
    """Opens the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    if request.method=='POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have been logged in!")
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Unable to register your account right now')

    else:
        registration_form = UserRegistrationForm()
    return render(request, "registration.html", {'registration_form': registration_form})

# Login
def login(request):
    """
    Opens the login page
    """
    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    if request.method=='POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(   username=request.POST['username'],
                                        password=request.POST['password'])
            if user:
                messages.success(request, 'successful login!')
                auth.login(user=user, request=request)
                return render(request, 'profile.html')
            else:
                login_form.add_error(None, 'Username or password are incorrect')

    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {'login_form': login_form})

# Logout
def logout(request):
    """Logs out any logged in users"""
    auth.logout(request)
    messages.success(request, 'Successful')
    return redirect(reverse('home'))
