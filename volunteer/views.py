from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from .models import Camp
from .forms import CampForm

# Authentication

#Register
def registration(request):
    """Opens the registration page"""
    return render(request, 'registration.html')

# Login
def login(request):
    """Opens the loginn page"""
    return render(request, 'login.html')

# Logout
def logout(request):
    """Logs out any logged in users"""
    auth.logout(request)
    messages.success(request, 'Successful')
    return redirect(reverse('get_camps'))

# List camps
def get_camps(request):
    """Open the camp list page and display any camps in list"""
    results = Camp.objects.all()
    return render(request, "camps.html", {'camps': results})

# Add a camp
def create_camp(request):
    """Opens the create a camp page add camp if method is POST"""
    if request.method=="POST":
        form = CampForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_camps)
    else:
        form = CampForm()
    return render(request, "camp_form.html", {'form': form})

# Edit existing camp
def edit_camp(request, id):
    """Opens the edit camp page. Save camp is method is POST"""
    camp = get_object_or_404(Camp, pk=id)

    if request.method=="POST":
        form = CampForm(request.POST, instance=camp)
        if form.is_valid():
            form.save()
            return redirect(get_camps)
    else:
        form = CampForm(instance=camp)
    return render(request, "camp_form.html", {'form': form})

