from management.models import *
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:

        model = Project
        fields = ['title', 'number', 'start_date', 'end_date', 'importance', 'abstract', 'result']
        # widgets = {
        #     'tests': forms.CheckboxSelectMultiple(),
        # }


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['title', 'number']
