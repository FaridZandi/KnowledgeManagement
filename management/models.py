from django.db import models
from multiselectfield import MultiSelectField
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




class ScientificActivity(models.Model):
    title = models.CharField(max_length=200)
    outputChoices = (('item_key1', 'دانش فنی'),
                     ('item_key2', 'ساخت'),
                     ('item_key3', 'فرآیند'),
                     ('item_key4', 'انسانی'),
                     ('item_key5', 'ارتباطی'),
                     ('item_key6', 'ساختاری'),
                     ('item_key7', 'ذینفعان'),
                     ('item_key8', 'نوآوری و فناوری'),
                     ('item_key9', 'روش های یادگیری'))

    output = MultiSelectField(choices=outputChoices)

    implicitPenChoices = (('item_key1', 'درس های آموخته شده'),
                          ('item_key2', 'مشکلات و ریسک های انجام شده'),
                          ('item_key3', 'فرآیندها و روش های اجرایی'),
                          ('item_key4', 'سایر'))

    implicit_scientific_pen = MultiSelectField(choices=implicitPenChoices)

    explicitPenChoices = (('item_key1', 'الگوها و قالب ها'),
                          ('item_key2', 'چک لیست ها'),
                          ('item_key3', 'راهنماها و دستورالعمل ها'),
                          ('item_key4', 'گزارش ها و وقایع نگارها'),
                          ('item_key5', 'سایر'),
                          ('item_key6', 'آیا برای انجام کار نیاز به نیروی دانشگر می باشد'))

    explicit_scientific_pen = MultiSelectField(choices=explicitPenChoices)


class ScientificArea(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    # TODO: in the forms change the widget to radio select
    is_main = models.BooleanField(name="نوع:", choices=[(True, "اصلی"), (False, "فرعی")])
    main_area = models.OneToOneField('ScientificArea', related_name='main_scientific_area', blank=True, null=True)

    moaChoices = (('item_key1', 'سرمایه های فکری'),
                  ('item_key2', 'روش های یادگیری'),
                  ('item_key3', 'نوآوری و فناوری'),
                  ('item_key4', 'ذینفعان'))

    activity_and_method_of_operation = MultiSelectField(name="فعالیت و شیوه ی کاری:", choices=moaChoices)

    intellectualPropertyChoices= (('item_key1', 'انسانی'),
                 ('item_key2', 'ساختاری'),
                 ('item_key3', 'ارتباطی'))

    intellectualProperty = MultiSelectField(name = "سرمایه های فکری:", choices=intellectualPropertyChoices)
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
    registration_code = models.CharField(20)
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
