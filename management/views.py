from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from django.views.generic import TemplateView, UpdateView, DeleteView
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
            projectForm=ProjectForm
        projects = Project.objects.all()
        return render(request, 'projectForm.html', {'projects' : projects, 'projectForm' : projectForm})


class PlanFormView(TemplateView):
    def get(self, request, *args, **kwargs):
        planForm = PlanForm
        return render(request, 'planForm.html', {'planForm' : planForm})

    def post(self, request, *args, **kwargs):
        planForm = PlanForm(request.POST)
        if planForm.is_valid():
            planForm.save()
            planForm=PlanForm
        return render(request, 'planForm.html', {'planForm' : planForm})

class PlanFormUpdateView(UpdateView):
    model = Plan
    fields = ['title', 'number']
    template_name = 'planFormUpdate.html'
    success_url = '/plan/new'

    # esm form va object ro chegoone mitavan taghiir dad ?


class PlanFormDeleteView(DeleteView):
    model = Plan
    template_name = 'planFormDelete.html'
    success_url = '/plan/new'
class ScientificActivityCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'scientificActivityCreate.html', {'form':ScientificActivityForm()})
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

class ScientificAreaCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'scientificAreaCreate.html', {'form':ScientificAreaForm})
    def post(self,request,*args,**kwargs):
        scientificAreaForm=ScientificAreaForm(request.POST)
        if(scientificAreaForm.is_valid()):
            scientificAreaForm.save()
            scientificAreaForm=ScientificAreaForm
        return render(request, 'scientificAreaCreate.html', {'form':scientificAreaForm})

class ScientificAreaUpdateView(UpdateView):
    model=ScientificArea
    form_class = ScientificAreaForm
    template_name = "scientificAreaUpdate.html"
    success_url = "/scientificarea/new/"

class ScientificAreaDeleteView(DeleteView):
    model=ScientificArea
    template_name = "scientificAreaDelete.html"
    success_url = "/scientificarea/new/"
    # return render(request, 'scientificAreaCreate.html', {'form':scientificAreaForm})

class DocumentationView(TemplateView):
    def get(self, request, *args, **kwargs ):
        return render(request, 'DocumentationCreate.html', {'form':DocumentationForm})

    def post(self, request, *args, **kwargs):
        documentationForm = DocumentationForm(request.POST)
        flag=False
        for i in range (1,int(request.POST['suggested-solution-count'])+1):
            str1 = 'suggested-solution-title-input-' + str(i)
            str2 = 'suggested-solution-body-input-' + str(i)
            if str1 in request.POST :
                if len(request.POST[str1]) > 0 or len(request.POST[str2]) > 0:
                    flag = True
                    break
        if not flag :
            documentationForm.add_error("","no suggested solution")
            return render(request, 'DocumentationCreate.html', {'form':documentationForm})

        minKeywordsCnt = 1
        flagCnt = 0
        for i in range (1, int(request.POST['keywords-count'])+1) :
            str1 = 'keywords-input-' + str(i)
            if str1 in request.POST and  len(request.POST[str1]) > 0 :
                flagCnt += 1
        if flagCnt < minKeywordsCnt :
            documentationForm.add_error("","not enough key words")
            return render(request, 'DocumentationCreate.html', {'form':documentationForm})


        if documentationForm.is_valid() :
            newDocumentation = documentationForm.save()
            documentationForm=DocumentationForm



        return render(request, 'DocumentationCreate.html', {'form':documentationForm})

