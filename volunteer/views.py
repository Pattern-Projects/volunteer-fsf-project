from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from .models import Camp
from .forms import CampForm

# Authentication

# Logout
def logout(request):
    auth.logout(request)
    messages.success(request, 'Successful')
    return redirect(reverse('get_camps'))

# List camps
def get_camps(request):
    results = Camp.objects.all()
    return render(request, "camps.html", {'camps': results})

# Add a camp
def create_camp(request):
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
    camp = get_object_or_404(Camp, pk=id)

    if request.method=="POST":
        form = CampForm(request.POST, instance=camp)
        if form.is_valid():
            form.save()
            return redirect(get_camps)
    else:
        form = CampForm(instance=camp)
    return render(request, "camp_form.html", {'form': form})

