from django.forms import ModelChoiceField

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

class ScientificActivityForm(forms.ModelForm):
    class Meta:
        model = ScientificActivity
        fields = ['title','output','implicit_scientific_pen','explicit_scientific_pen']
        widgets = {'output': forms.CheckboxSelectMultiple(),'implicit_scientific_pen':forms.CheckboxSelectMultiple(),'explicit_scientific_pen':forms.CheckboxSelectMultiple()}

class ScientificAreaForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ScientificAreaForm,self).__init__(*args,**kwargs)
        self.fields['main_area'].queryset=ScientificArea.objects.filter(is_main=True)

    class Meta:
        model = ScientificArea
        fields='__all__'
        widgets={'is_main':forms.RadioSelect(),'activity_and_method_of_operation':forms.CheckboxSelectMultiple(),'intellectualProperty':forms.CheckboxSelectMultiple(),'is_potential':forms.RadioSelect()}


