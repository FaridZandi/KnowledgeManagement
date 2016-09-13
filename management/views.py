from django.shortcuts import render
from django.views.generic import TemplateView
from management.models import *
from management.forms import *

# Create your views here.

class projectFormView(TemplateView):

    def get(self, request, *args, **kwargs):
        # projects = Project.objects.all()
        projectForm = ProjectForm
        # return render(request, 'projectForm.html', {'projects': projects, 'projectForm': projectForm})

    def post(self, request, *args, **kwargs):
        projectForm = ProjectForm(request.POST)
        if projectForm.is_valid():
            projectForm.save()
            projectForm.seve_m2m()
        # projects = Project.objects.all()
        projectForm = ProjectForm
        # return render(request, 'projectForm.html', {'projects' : projects, 'projectForm' : projectForm})

    #salam