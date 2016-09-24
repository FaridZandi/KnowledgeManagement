from itertools import chain
from operator import attrgetter

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
        self.fields['main_area'].queryset = ScientificArea.objects.filter(is_main=True)
        if len(self.fields['main_area'].queryset) != 0:
            self.fields['main_area'].empty_label = None

    class Meta:
        model = ScientificArea
        fields='__all__'
        widgets={'is_main':forms.RadioSelect(),'activity_and_method_of_operation':forms.CheckboxSelectMultiple(),'intellectualProperty':forms.CheckboxSelectMultiple(),'is_potential':forms.RadioSelect()}


class DocumentationForm(forms.ModelForm):
    class Meta:
        model = Documentation
        exclude = ('date',)


class SciencePackageTopicForm(forms.ModelForm):
    # plan = forms.ModelChoiceField(queryset=Plan.objects.all())
    # project = forms.ModelChoiceField(queryset=Project.objects.all())

    def __init__(self, *args, **kwargs):
        super(SciencePackageTopicForm, self).__init__(*args, **kwargs)
        if len(self.fields['plan'].queryset) != 0:
            self.fields['plan'].empty_label = None

        if len(self.fields['project'].queryset) != 0:
            self.fields['project'].empty_label = None

    class Meta:
        model = SciencePackageTopic
        fields = ['plan', 'project', 'title', 'description']


class SciencePackageForm(forms.ModelForm):
    # plan = forms.ModelChoiceField(queryset=Plan.objects.all())
    # project = forms.ModelChoiceField(queryset=Project.objects.all())

    def __init__(self, *args, **kwargs):
        super(SciencePackageForm, self).__init__(*args, **kwargs)
        if len(self.fields['plan'].queryset) != 0:
            self.fields['plan'].empty_label = None

        if len(self.fields['project'].queryset) != 0:
            self.fields['project'].empty_label = None

        if len(self.fields['scientificArea'].queryset) != 0:
            self.fields['scientificArea'].empty_label = None

        if len(self.fields['science_package_topic'].queryset) != 0:
            self.fields['science_package_topic'].empty_label = None

    class Meta:
        model = SciencePackage
        fields = ['plan', 'project', 'product_name', 'product_science', 'product_features', 'title', 'scientificArea',
                  'science_package_topic', 'lessons', 'skills', 'tools']
