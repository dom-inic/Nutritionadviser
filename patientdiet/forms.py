from django.forms import ModelForm
from . models import Personal_details, Health_details
from django import forms

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal_details
        fields = ['name', 'id_no', 'dob', 'age', 'place_of_residency', 'contact', 'patient_number', 'date_of_visit', 'gender', 'email', 'county']
        label = {'name': ''}

class HealthForm(forms.ModelForm):
    class Meta:
        model = Health_details
        fields = ['names', 'patient_number', 'previously_diagnised_disease', 'currently_diagonised_disease',
        'year_diagonised', 'allergies', 'weight', 'height', 'bmi', 'muac', 'on_arvs', 'cd4_count','tca', 'clinician_designation',
        'diet', 'condition', 'disease', 'medicine_prescribed', 'clinician' ]
        label = {'names': ''}



