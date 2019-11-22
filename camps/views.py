from django.shortcuts import render, get_object_or_404, redirect
from .models import Camp, FilterModel
from .forms import CampForm, FilterForm

def get_camps(request):
    """
    Create a view that will return a list
    of Camps and render them to the 'camps.html' template
    """
    model = FilterModel()

    # TODO:Repair or remove
    if request.method == "POST":
        form = FilterForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            model = form.save()
            results = Camp.objects.filter(model)[:30]
    else:
        form = FilterForm(instance=model)
        results = Camp.objects.order_by('published_date')[:30]

    return render(request, "camps.html", {'camps': results, 'form': form})

def camp_details(request, pk):
    """
    Create a view that returns a single
    Camp object based on the camp ID (pk) and
    render it with the 'camp.html' template.
    Or return a 404 if the camp is not found
    """
    camp = get_object_or_404(Camp, pk=pk)
    camp.save()
    return render(request, "camp.html", {'camp': camp})

def filter_by_continent (request, continent):
    """
    Return a list of camps where camp.continent
    is equal to given continent
    """
    print(continent)
    results = Camp.objects.filter(continent=continent)[:30]
    return render(request, "camps.html", {'camps': results})


def create_or_edit_a_volunteer_camp(request, pk=None):
    """
    Create a view that is used to create
    or edit a volunteer camp depending on the Camp ID
    And rendering it to the 'edit_camp.html' template
    """
    camp = get_object_or_404(Camp, pk=pk) if pk else None
    if request.method == "POST":
        form = CampForm(request.POST, request.FILES, instance=camp)
        if form.is_valid():
            camp = form.save()
            return redirect(get_camps)
    else:
        form = CampForm(instance=camp)
    return render(request, 'edit_camp.html', {'form': form})

def archive_camp(request, pk=None):
    """
    Change the camp archive setting to true
    """
    camp = get_object_or_404(Camp, pk=pk)
    camp.archived = True
    camp.save()
    return redirect('get_archived_camps')

def get_archived_camps(request):
    """
    Show a list of archived camps
    """
    results = Camp.objects.filter(archived=True)
    return render(request, "camps.html", {'camps': results})

def delete_camp(request, pk=None):
    """
    Delete camp of given pk as id
    """
    Camp.objects.filter(id=pk).delete()
    return redirect(get_camps)
