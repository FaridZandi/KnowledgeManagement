from django.contrib import admin
from .models import *
# Register your models here.


class SuggestedSolutionAdminInline (admin.TabularInline):
    model= DocumentationSuggestedSolution
    extra = 0


class KeywordAdminInline (admin.TabularInline):
    model = DocumentationKeyword
    extra = 0


class DocumentationAdmin(admin.ModelAdmin):
    inlines = (SuggestedSolutionAdminInline, KeywordAdminInline, )


class PlanGoalInLine(admin.TabularInline):
    model = PlanGoal
    extra = 0

class PlanAdmin(admin.ModelAdmin):
    inlines = (PlanGoalInLine,)

admin.site.register(Project)
admin.site.register(ScientificArea)
admin.site.register(OutputChoice)
admin.site.register(ScientificActivity)
admin.site.register(ImplicitPenChoices)
admin.site.register(ExplicitPenChoices)
admin.site.register(IntellectualPropertyChoice)
admin.site.register(Documentation, DocumentationAdmin)
admin.site.register(MoaChoice)
admin.site.register(Plan, PlanAdmin)
admin.site.register(PlanGoal)


