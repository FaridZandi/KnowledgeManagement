from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import RegexValidator
from django.db import models
# Create your models here.


class Plan(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=200)
    number = models.CharField(verbose_name="شماره طرح", unique=True, max_length=20,
                              validators=[RegexValidator(regex=r'^\d+$', message="این فیلد تنها میتواند شامل کاراکتر های عددی باشد.")])

    def __str__(self):
        return self.title


class PlanGoal(models.Model):
    body = models.TextField(verbose_name="متن")
    plan = models.ForeignKey(Plan, related_name="goals")

    def __str__(self):
        return self.body


class Project(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=200)
    number = models.CharField(verbose_name="شماره پروژه", unique=True, max_length=20,
                              validators=[RegexValidator(regex=r'^\d+$', message="این فیلد تنها میتواند شامل کاراکتر های عددی باشد.")])
    start_date = models.DateField(verbose_name="تاریخ شروع", blank=True, null=True)
    end_date = models.DateField(verbose_name="تاریخ پایان", blank=True, null=True)
    importance = models.TextField(verbose_name="اهمیت")
    abstract = models.TextField(verbose_name="چکیده")
    result = models.TextField(verbose_name="نتیجه گیری")
    plan = models.ForeignKey(Plan, related_name="projects")

    def __str__(self):
        return self.title


class ProjectGoal(models.Model):
    body = models.TextField(verbose_name="متن")
    project = models.ForeignKey(Project, related_name="goals")


class ProjectStep(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=200, blank=True, null=True)
    body = models.TextField(verbose_name="متن", blank=True, null=True)
    project = models.ForeignKey(Project, related_name="steps")


class ProjectExecutor(models.Model):
    role = models.CharField(verbose_name="نقش", max_length=200)
    name = models.CharField(verbose_name="نام", max_length=200)
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
    title = models.CharField(verbose_name="عنوان", max_length=200)
    output = models.ManyToManyField(OutputChoice, verbose_name="خروجی فعالیت")
    implicit_scientific_pen = models.ManyToManyField(ImplicitPenChoices, verbose_name="قلم دانشی(ضمنی)")
    explicit_scientific_pen = models.ManyToManyField(ExplicitPenChoices, verbose_name="قلم دانشی(صریح)")
    # TODO : add this field to form as a checkbox
    Is_knowledge_worker_needed = models.BooleanField(verbose_name="آيا براي انجام كار نياز به نيروي دانشگر ميباشد", default=False)


class MoaChoice(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class IntellectualPropertyChoice(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ScientificArea(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=200)
    summary = models.TextField(verbose_name="شرح مختصر")
    is_main = models.BooleanField(verbose_name="نوع:", choices=[(True, "اصلی"), (False, "فرعی")],default=True)
    main_area = models.ForeignKey(to="ScientificArea", default=None, blank=True, null=True,
                                  related_name='main_scientific_area', verbose_name="حوزه اصلی")

    activity_and_method_of_operation = models.ManyToManyField(MoaChoice,verbose_name="فعالیت و شیوه ی کاری:",blank=True)

    intellectualProperty = models.ManyToManyField(IntellectualPropertyChoice, verbose_name = "سرمایه های فکری:",blank=True)
    learning_methods = models.TextField(verbose_name="روش های یادگیری", null=True, blank=True)
    innovation_and_technology = models.TextField(verbose_name="نوآوری و فناوری", null=True, blank=True)
    beneficiaries = models.TextField(verbose_name="ذینفعان", null=True, blank=True)

    is_essential = models.BooleanField(verbose_name= "حیاتی برای پروژه.", default=False)
    is_effective = models.BooleanField(verbose_name= "در انجام پروژه موثر است.", default=False)
    is_potential = models.BooleanField(verbose_name="تاثیر ", choices=[(True, "بالقوه"), (False, "بالفعل")], default=False)

    def __str__(self):
        return self.title


class Paper(models.Model):
    name = models.CharField(verbose_name="نام", max_length=200)
    publish_date = models.DateField(verbose_name="تاریخ انتشار")


class PaperAuthor(models.Model):
    national_code = models.CharField(verbose_name="کد ملی", max_length=20)
    company_registration_code = models.CharField(verbose_name="کد ثبت شرکت", max_length=20)
    Paper = models.ForeignKey(Paper, related_name='authors')


class Thesis(models.Model):
    name = models.CharField(verbose_name="نام", max_length=200)
    publish_date = models.DateField(verbose_name="تاریخ انتشار")
    author_national_code = models.CharField(verbose_name="کد ملی نویسنده", max_length=10)


class Invention(models.Model):
    name = models.CharField(verbose_name="نام", max_length=200)
    registration_code = models.CharField(verbose_name="کد ثبت", max_length=20)
    registration_date = models.DateField(verbose_name="تاریخ ثبت")


class Inventor(models.Model):
    national_code = models.CharField(verbose_name="کد ملی", max_length=10)
    company_registration_code = models.CharField(verbose_name="کد ثبت شرکت", max_length=20)
    invention = models.ForeignKey(Invention, related_name="inventors")


class ScientificDocument(models.Model):
    name = models.CharField(verbose_name="نام", max_length=200)
    owner_national_code = models.CharField(verbose_name="کد ملی دارنده", max_length=10)


class ScientificRank(models.Model):
    name = models.CharField(verbose_name="نام", max_length=200)
    related_company_registration_code = models.CharField(verbose_name="کد ثبت شرکت مرتبط", max_length=20)


class ExternalResource(models.Model):
    name = models.CharField(verbose_name="عنوان", max_length=200)
    link = models.URLField(verbose_name="لینک")


class Documentation(models.Model):
    date = models.DateField()
    registration_number = models.CharField(verbose_name="شماره ثبت", max_length=20,
                                           validators=[RegexValidator(regex=r'^\d+$',message="این فیلد تنها میتواند شامل کاراکتر های عددی باشد.")])
    # TODO : still no Person Model so I can't add this one
    person = "to be added"
    role = models.CharField(verbose_name="نقش در پروژه", max_length=200)
    project = models.ForeignKey(Project)
    activity = models.CharField(verbose_name="عنوان فعالیت", max_length=200)
    problem_title = models.CharField(verbose_name="عنوان مشکل", max_length=200)
    problem_description = models.TextField(verbose_name="شرح مشکل و دلایل")


class DocumentationSuggestedSolution(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=200, null=True, blank=True)
    description = models.TextField(verbose_name="متن", null=True, blank=True)
    documentation = models.ForeignKey(Documentation, related_name="solutions")


class DocumentationKeyword(models.Model):
    name = models.CharField(verbose_name="کلمه کلیدی", max_length=100)
    documentation = models.ForeignKey(Documentation, related_name="keywords")


class SciencePackageTopic(models.Model):
    # TODO: in the form a radio button must be shown to choose between plans and project. Each one checked will be shown
    project = models.ForeignKey(Project, verbose_name="پروژه", null=True, blank=True)
    plan = models.ForeignKey(Plan, verbose_name="طرح", null=True, blank=True)

    title = models.CharField(verbose_name="عنوان", max_length=200)
    description = models.TextField(verbose_name="شرح مختصر")


class SciencePackage(models.Model):
    # TODO: in the form a radio button must be shown to choose between plans and project. Each one checked will be shown
    project = models.ForeignKey(Project)
    plan = models.ForeignKey(Plan)

    product_name = models.CharField(verbose_name="نام محصول", max_length=200)
    product_science = models.TextField(verbose_name="دانش فنی مرتبط با محصول")
    product_features = models.TextField(verbose_name="ویژگی های محصول")

    # TODO: a table of person objects is needed for this model as تهیه کننده گان دانش

    title = models.CharField(max_length=200)
    scientificArea = models.ForeignKey(ScientificArea)

    science_package_topic = models.ForeignKey(SciencePackageTopic, verbose_name="سرفصل بسته ی دانش")

    lessons = models.TextField(verbose_name="دانش های آموخته شده")
    skills = models.TextField(verbose_name="مهارت ها و تکنیک های حاصله")
    # TODO: a table of person objects in needed fot this part as مشخصات دانشگران مرتبط
    tools = models.TextField(verbose_name="ابزار و تجهیزات")




