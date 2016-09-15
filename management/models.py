from django.db import models
# Create your models here.


class Plan(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    def __str__(self):
        return self.title


class PlanGoal(models.Model):
    body = models.TextField()
    project = models.ForeignKey(Plan, related_name="goals")


class Project(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    importance = models.TextField()
    abstract = models.TextField()
    result = models.TextField()
    plan = models.ForeignKey(Plan, related_name="projects")


class ProjectGoal(models.Model):
    body = models.TextField()
    project = models.ForeignKey(Project, related_name="goals")


class ProjectStep(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    project = models.ForeignKey(Project, related_name="steps")


class ProjectExecutor(models.Model):
    role = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, related_name="executors")


class OutputChoice(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class ImplicitPenChoices(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class ExplicitPenChoices(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class ScientificActivity(models.Model):
    title = models.CharField(max_length=200)
    output = models.ManyToManyField(OutputChoice)
    implicit_scientific_pen = models.ManyToManyField(ImplicitPenChoices)
    explicit_scientific_pen = models.ManyToManyField(ExplicitPenChoices)


class MoaChoice(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class IntellectualPropertyChoice(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class ScientificArea(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    # TODO: in the forms change the widget to radio select
    is_main = models.BooleanField(verbose_name="نوع:", choices=[(True, "اصلی"), (False, "فرعی")],default=True)

    main_area = models.ForeignKey(to="ScientificArea", related_name='main_scientific_area', blank=True, null=True)

    activity_and_method_of_operation = models.ManyToManyField(MoaChoice,verbose_name="فعالیت و شیوه ی کاری:",blank=True,null=True)

    intellectualProperty = models.ManyToManyField(IntellectualPropertyChoice, verbose_name = "سرمایه های فکری:",blank=True,null=True)
    learning_methods = models.TextField(null=True, blank=True)
    innovation_and_technology = models.TextField(null=True, blank=True)
    beneficiaries = models.TextField(null=True, blank=True)

    is_essential = models.BooleanField(verbose_name= "حیاتی برای پروژه.", default=False)

    is_effective = models.BooleanField(verbose_name= "در انجام پروژه موثر است.", default=False)

    is_potential = models.BooleanField(verbose_name="تاثیر ", choices=[(True, "بالقوه"), (False, "بالفعل")], default=False)

    def __str__(self):
        return self.title


class Paper(models.Model):
    name = models.CharField(max_length=200)
    publish_date = models.DateField()


class PaperAuthor(models.Model):
    national_code = models.CharField(max_length=20)
    company_registration_code = models.CharField(max_length=20)
    Paper = models.ForeignKey(Paper, related_name='authors')


class Thesis(models.Model):
    name = models.CharField(max_length=200)
    publish_date = models.DateField()
    author_national_code = models.CharField(max_length=10)


class Invention(models.Model):
    name = models.CharField(max_length=200)
    registration_code = models.CharField(max_length=20)
    registration_date = models.DateField()


class Inventor(models.Model):
    national_code = models.CharField(max_length=10)
    company_registration_code = models.CharField(max_length=20)
    invention = models.ForeignKey(Invention, related_name="inventors")


class ScientificDocument(models.Model):
    name = models.CharField(max_length=200)
    owner_national_code = models.CharField(max_length=10)


class ScientificRank(models.Model):
    name = models.CharField(max_length=200)
    related_company_registration_code = models.CharField(max_length=20)


class ExternalResource(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()


class Documentation(models.Model):
    date = models.DateField()
    registration_code = models.CharField(max_length=20)
    # TODO : still no Person Model so I can't add this one
    person = "to be added"
    role = models.CharField(max_length=200)
    project = models.ForeignKey(Project)
    activity = models.CharField(max_length=200)
    problem_title = models.CharField(max_length=200)
    problem_description = models.TextField()


class DocumentationSuggestedSolution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    documentation = models.ForeignKey(Documentation, related_name="solutions")


class DocumentationKeyword(models.Model):
    name = models.CharField(max_length=100)
    documentation = models.ForeignKey(Documentation, related_name="keywords")


class ScientificPackage(models.Model):
    title = models.CharField(max_length=200)
    scientificArea = models.ForeignKey(ScientificArea)


    project = models.ForeignKey(Project)
    plan = models.ForeignKey(Plan)
