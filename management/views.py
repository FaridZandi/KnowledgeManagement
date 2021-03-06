from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView, UpdateView, DeleteView
from management.models import *
from management.forms import *
from datetime import date
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

        keys = list(request.POST.keys())
        keys = [k for k in keys if (k.startswith("plan-goal-input") and len(request.POST[k]) > 0)]

        if len(keys) == 0:
            planForm.add_error("","حداقل یک هدف اضافه کنید")
            return render(request, 'planForm.html', {'planForm' : planForm})

        if planForm.is_valid():
            newPlan = planForm.save()
            planForm = PlanForm
            for k in keys:
                PlanGoal.objects.create(body=request.POST[k], plan=newPlan)

        return render(request, 'planForm.html', {'planForm' : planForm})

class PlanFormUpdateView(UpdateView):
    model = Plan
    fields = ['title', 'number']
    template_name = 'planFormUpdate.html'
    success_url = '/plan/new'


    def get_context_data(self, **kwargs):
        context = super(PlanFormUpdateView,self).get_context_data(**kwargs)
        context['goals'] = self.object.goals.all()
        context['number'] = len(self.object.goals.all())
        return context


    def post(self, request, *args, **kwargs):
        planForm = PlanForm(request.POST, instance=self.get_object())

        keys = list(request.POST.keys())
        keys = [k for k in keys if (k.startswith("plan-goal-input") and len(request.POST[k]) > 0)]
        keys.sort()

        if len(keys) == 0:
            planForm.add_error("","حداقل یک هدف اضافه کنید")
            return render(request, 'planFormUpdate.html', {'planForm' : planForm})

        if planForm.is_valid():
            newPlan = planForm.save()
            planForm = PlanForm

            self.get_object().goals.all().delete()

            for k in keys:
                PlanGoal.objects.create(body=request.POST[k], plan=newPlan)
            return HttpResponseRedirect(self.success_url)

# esm form va object ro chegoone mitavan taghiir dad ?


class PlanFormDeleteView(DeleteView):
    model = Plan
    template_name = 'planFormDelete.html'
    success_url = '/plan/new'


class ScientificActivityCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'scientificActivityCreate.html', {'form':ScientificActivityForm()})

    def post(self, request, *args, **kwargs):
        scientific_activity_form = ScientificActivityForm(request.POST)
        if scientific_activity_form.is_valid():
            scientific_activity_form.save()
            scientific_activity_form = ScientificActivityForm

        return render(request, 'scientificActivityCreate.html', {'form': scientific_activity_form})


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

        if documentationForm.is_valid():
            newDocumentation = documentationForm.save(commit=False)
            newDocumentation.date = date.today()
            newDocumentation.save()
            documentationForm.save_m2m()
            documentationForm=DocumentationForm

            for i in range (1,int(request.POST['suggested-solution-count'])+1):
                str1 = 'suggested-solution-title-input-' + str(i)
                str2 = 'suggested-solution-body-input-' + str(i)
                if str1 in request.POST :
                    if len(request.POST[str1]) > 0 or len(request.POST[str2]) > 0:
                        DocumentationSuggestedSolution.objects.create(title=request.POST[str1], description=request.POST[str2], documentation=newDocumentation)

            for i in range (1, int(request.POST['keywords-count'])+1) :
                str1 = 'keywords-input-' + str(i)
                if str1 in request.POST and  len(request.POST[str1]) > 0 :
                    DocumentationKeyword.objects.create(name=request.POST[str1], documentation=newDocumentation)
        else:
            return HttpResponse(documentationForm.errors)


        return render(request, 'DocumentationCreate.html', {'form':documentationForm})


class SciencePackageCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        science_package_form = SciencePackageForm
        return render(request, 'SciencePackageCreate.html', {'science_package_form': science_package_form})

    def post(self, request, *args, **kwargs):
        science_package_form = SciencePackageForm(request.POST)
        if science_package_form.is_valid():
            new_science_package = science_package_form.save(commit=False)

            if 'plan_or_project' in request.POST:

                value = request.POST['plan_or_project']
                if value == 'plan':
                    new_science_package.project = None
                if value == 'project':
                    new_science_package.plan = None

            if (new_science_package.plan is None) and (new_science_package.project is None):
                science_package_form.add_error("", "هیچ طرح یا پروژه ای انتخاب نشده است.")
                return render(request, 'SciencePackageCreate.html', {'science_package_form': science_package_form})
            new_science_package.save()
            science_package_form = SciencePackageForm
        return render(request, 'SciencePackageCreate.html', {'science_package_form': science_package_form})


class SciencePackageUpdateView(UpdateView):
    model = SciencePackage
    success_url = '/sciencepackage/new'
    template_name = 'SciencePackageUpdate.html'
    form_class = SciencePackageForm

    def get_context_data(self, **kwargs):
        data = super(SciencePackageUpdateView, self).get_context_data(**kwargs)
        data['science_package_form'] = data.get('form')

        if self.object.project is None:
            data['plan_or_project'] = 'plan'
        else:
            data['plan_or_project'] = 'project'
        return data

    def post(self, request, pk, *args, **kwargs):
        form = SciencePackageForm(request.POST, instance=self.get_object())
        if form.is_valid():
            updated_object = form.save(commit=False)
            if 'plan_or_project' in self.request.POST:
                value = request.POST['plan_or_project']
                if value == 'plan':
                    updated_object.project = None
                if value == 'project':
                    updated_object.plan = None

                if (updated_object.plan is None) and (updated_object.project is None):
                    form.add_error("", "هیچ طرح یا پروژه ای انتخاب نشده است.")
                    return render(request, 'SciencePackageUpdate.html', {'science_package_form': form})
            updated_object.save()
            return HttpResponseRedirect(self.success_url)
        return render(self.request, 'SciencePackageUpdate.html', {'science_package_form': form})


class SciencePackageDeleteView(DeleteView):
    model = SciencePackage
    template_name = 'SciencePackageDelete.html'
    success_url = '/sciencepackage/new/'


class SciencePackageTopicCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        science_package_topic_form = SciencePackageTopicForm
        return render(request, 'SciencePackageTopicCreate.html', {'science_package_topic_form': science_package_topic_form})

    def post(self, request, *args, **kwargs):
        science_package_topic_form = SciencePackageTopicForm(request.POST)
        if science_package_topic_form.is_valid():
            new_science_package_topic = science_package_topic_form.save(commit=False)

            if 'plan_or_project' in request.POST:

                value = request.POST['plan_or_project']
                if value == 'plan':
                    new_science_package_topic.project = None
                if value == 'project':
                    new_science_package_topic.plan = None

            if (new_science_package_topic.plan is None) and (new_science_package_topic.project is None):
                science_package_topic_form.add_error("", "هیچ طرح یا پروژه ای انتخاب نشده است.")
                return render(request, 'SciencePackageTopicCreate.html', {'science_package_topic_form': science_package_topic_form})
            new_science_package_topic.save()
            science_package_topic_form = SciencePackageTopicForm
        return render(request, 'SciencePackageTopicCreate.html', {'science_package_topic_form': science_package_topic_form})


class SciencePackageTopicUpdateView(UpdateView):
    model = SciencePackageTopic
    template_name = 'SciencePackageTopicUpdate.html'
    success_url = '/sciencepackagetopic/new/'
    form_class = SciencePackageTopicForm

    def get_context_data(self, **kwargs):
        data = super(SciencePackageTopicUpdateView, self).get_context_data(**kwargs)
        data['science_package_topic_form'] = data.get('form')

        if self.object.project is None:
            data['plan_or_project'] = 'plan'
        else:
            data['plan_or_project'] = 'project'
        return data

    def post(self, request, pk, *args, **kwargs):
        form = SciencePackageTopicForm(request.POST, instance=self.get_object())
        if form.is_valid():
            updated_object = form.save(commit=False)
            if 'plan_or_project' in self.request.POST:
                value = request.POST['plan_or_project']
                if value == 'plan':
                    updated_object.project = None
                if value == 'project':
                    updated_object.plan = None

                if (updated_object.plan is None) and (updated_object.project is None):
                    form.add_error("", "هیچ طرح یا پروژه ای انتخاب نشده است.")
                    return render(request, 'SciencePackageTopicUpdate.html', {'science_package_topic_form': form})
            updated_object.save()
            return HttpResponseRedirect(self.success_url)
        return render(self.request, 'SciencePackageTopicUpdate.html', {'science_package_topic_form': form})


class SciencePackageTopicDeleteView(DeleteView):
    model = SciencePackageTopic
    template_name = 'SciencePackageTopicDelete.html'
    success_url = '/sciencepackagetopic/new/'


class DocumentationDeleteView(DeleteView):
    model = Documentation
    template_name = 'DocumentationDelete.html'
    success_url = '/documentation/new'


class DocumentationUpdateView(UpdateView):
    model=Documentation
    form_class = DocumentationForm
    template_name = "documentationUpdate.html"
    success_url = "/documentation/new/"

    def get_context_data(self, **kwargs):
        context = super(DocumentationUpdateView, self).get_context_data(**kwargs)
        context['documentation_suggested_solution'] = self.object.solutions.all()
        context['documentation_keyword'] = self.object.keywords.all()
        return context

    def post(self, request, *args, **kwargs):
        form = DocumentationForm(request.POST, instance=self.get_object())
        documentationForm = form
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
            return render(request, 'documentationUpdate.html', {'form':documentationForm,'documentation_suggested_solution':self.get_object().solutions.all(),'documentation_keyword':self.get_object().keywords.all() })

        minKeywordsCnt = 1
        flagCnt = 0
        for i in range (1, int(request.POST['keywords-count'])+1) :
            str1 = 'keywords-input-' + str(i)
            if str1 in request.POST and  len(request.POST[str1]) > 0 :
                flagCnt += 1
        if flagCnt < minKeywordsCnt :
            documentationForm.add_error("","not enough key words")
            return render(request, 'documentationUpdate.html', {'form':documentationForm,'documentation_suggested_solution':self.get_object().solutions.all(),'documentation_keyword':self.get_object().keywords.all() })

        if documentationForm.is_valid():
            self.get_object().solutions.all().delete()
            self.get_object().keywords.all().delete()
            newDocumentation = documentationForm.save(commit=False)
            newDocumentation.date = date.today()
            newDocumentation.save()

            for i in range (1,int(request.POST['suggested-solution-count'])+1):
                str1 = 'suggested-solution-title-input-' + str(i)
                str2 = 'suggested-solution-body-input-' + str(i)
                if str1 in request.POST :
                    if len(request.POST[str1]) > 0 or len(request.POST[str2]) > 0:
                        DocumentationSuggestedSolution.objects.create(title=request.POST[str1], description=request.POST[str2], documentation=newDocumentation)

            for i in range (1, int(request.POST['keywords-count'])+1) :
                str1 = 'keywords-input-' + str(i)
                if str1 in request.POST and  len(request.POST[str1]) > 0 :
                    DocumentationKeyword.objects.create(name=request.POST[str1], documentation=newDocumentation)
        else:
            return HttpResponse(documentationForm.errors)


        return HttpResponseRedirect(self.success_url)
