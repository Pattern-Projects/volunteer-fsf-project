from django.shortcuts import render, HttpResponse, redirect
from .models import Camp
from .forms import CampForm

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