from django.shortcuts import render, HttpResponse, redirect
from .models import Camp

# List camps
def get_camps(request):
    results = Camp.objects.all()
    return render(request, "camps.html", {'camps': results})
    
# Add a camp
def create_camp(request):
    if request.method=="POST":
        new_camp = Camp()
        new_camp.name = request.POST.get('name')
        new_camp.available = 'available' in request.POST
        new_camp.save()
        return redirect(get_camps)
    return render(request, "camp_form.html")