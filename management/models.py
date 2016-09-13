from django.db import models
# Create your models here.


class Plan(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=20)


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


class ImplicitPenChoices(models.Model):
    name = models.CharField(max_length=30)


class ExplicitPenChoices(models.Model):
    name = models.CharField(max_length=30)


class ScientificActivity(models.Model):
    title = models.CharField(max_length=200)
    output = models.ManyToManyField(OutputChoice)
    implicit_scientific_pen = models.ManyToManyField(ImplicitPenChoices)
    explicit_scientific_pen = models.ManyToManyField(ExplicitPenChoices)


class MoaChoice(models.Model):
    name = models.CharField(max_length=20)


class IntellectualPropertyChoice(models.Model):
    name = models.CharField(max_length=30)


class ScientificArea(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    # TODO: in the forms change the widget to radio select
    is_main = models.BooleanField(name="نوع:", choices=[(True, "اصلی"), (False, "فرعی")])
    main_area = models.OneToOneField('ScientificArea', related_name='main_scientific_area', blank=True, null=True)

    activity_and_method_of_operation = models.ManyToManyField(MoaChoice,name="فعالیت و شیوه ی کاری:")

    intellectualProperty = models.ManyToManyField(IntellectualPropertyChoice, name = "سرمایه های فکری:")
    learning_methods = models.TextField()
    innovation_and_technology = models.TextField()
    beneficiaries = models.TextField()

    is_essential = models.BooleanField(name = "حیاتی برای پروژه.")

    is_effective = models.BooleanField(name = "در انجام پروژه موثر است.")

    is_potential = models.BooleanField(name=" ", choices=[(True, "بالقوه"), (False, "بالفعل")])


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
    project = models.OneToOneField(Project)
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


