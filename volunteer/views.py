from django.shortcuts import render
from .models import Camp

# Create your views here.
def get_camps(request):
    results = Camp.objects.all()
    return render(request, "camps.html", {'camps': results})