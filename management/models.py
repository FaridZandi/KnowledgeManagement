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
    start_data = models.DateField(blank=True, null=True)
    end_data = models.DateField(blank=True, null=True)
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
    is_main = models.BooleanField("نوع:")
    main_area = models.OneToOneField(ScientificActivity, related_name='main_area', blank=True, null=True)



