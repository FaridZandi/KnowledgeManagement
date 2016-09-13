from django.shortcuts import render
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from management.models import *
from management.forms import *

# Create your views here.


class projectFormView(TemplateView):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        projectForm = ProjectForm
        return render(request, 'projectForm.html', {'projects': projects, 'projectForm': projectForm})

    def post(self, request, *args, **kwargs):
        projectForm = ProjectForm(request.POST)
        if projectForm.is_valid():
            projectForm.save()
            projectForm.seve_m2m()
        projects = Project.objects.all()
        projectForm = ProjectForm
        return render(request, 'projectForm.html', {'projects' : projects, 'projectForm' : projectForm})


class PlanFormView(TemplateView):
    def get(self, request, *args, **kwargs):
        planForm = PlanForm
        return render(request, 'planForm.html', {'planForm' : planForm})

    def post(self, request, *args, **kwargs):
        planForm = PlanForm(request.POST)
        if planForm.is_valid():
            planForm.save()
        planForm = PlanForm
        return render(request, 'planForm.html', {'planForm' : planForm})

class ScientificActivityCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'scientificActivityCreate.html', {'form':ScientificActivityForm})
    def post(self,request,*args,**kwargs):
        scientificActivityForm=ScientificActivityForm(request.POST)
        if(scientificActivityForm.is_valid()):
            scientificActivityForm.save()
        scientificActivityForm=ScientificActivityForm
        return render(request, 'scientificActivityCreate.html', {'form':scientificActivityForm})

class ScientificActivityUpdateView(UpdateView):
    model=ScientificActivity
    form_class = ScientificActivityForm
    template_name = "scientificActivityUpdate.html"
    success_url = "/scientificactivity/new/"

class ScientificActivityDeleteView(DeleteView):
    model=ScientificActivity
    template_name = "scientificActivityDelete.html"
    success_url = "/scientificactivity/new/"
