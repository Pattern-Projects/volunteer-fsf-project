from django.shortcuts import render, redirect
from camps.views import get_camps
from camps.models import Camp, FilterModel
from camps.forms import FilterForm
from django.db.models import Q


# Create your views here.
def search_camps(request):
    query = request.GET['query']
    camps = Camp.objects.filter(Q(title__icontains=query) | Q(region__icontains=query) | Q(country__icontains=query) | Q(continent__icontains=query) | Q(required_language__icontains=query))
    model = FilterModel()
    filter = FilterForm(instance=model)

    return render(request, 'camps.html', {'camps':camps, 'form': filter})