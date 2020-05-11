from django.shortcuts import render
from django.http import HttpResponse
from . forms import PersonalForm, HealthForm
from django.shortcuts import reverse
from django.http import HttpResponseRedirect

def index(request):
    template_name = 'patientdiet/index.html'
    return render(request, template_name)

def new_profile(request):
    """ allow the patient to create a new profile"""
    if request.method != 'POST':
        # no data has been submitted, therefor we create a blank form
        # we create an instance of the class PersonalForm
        form = PersonalForm()
    else:
        # post the data submitted and process the data
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('health_details'))

    context = {'form':form}
    template_name = 'patientdiet/new_profile.html'
    return render(request, template_name, context)

def health_details(request):
    """ allow the user to provide health details """
    if request.method != 'POST':
        # no data has been submitte so we create a new form 
        # we create an instance of the class HealthForm
        form = HealthForm()

    else:
        # post the data submitted and process it
        form = HealthForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diet'))

    context = {'form':form}
    template_name = 'patientdiet/health.html'
    return render(request, template_name, context)
def diet(request):
    template_name = 'patientdiet/diet.html'
    return render(request, template_name)





    




