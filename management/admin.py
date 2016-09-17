from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(ScientificArea)
admin.site.register(OutputChoice)
admin.site.register(ScientificActivity)
admin.site.register(ImplicitPenChoices)
admin.site.register(ExplicitPenChoices)
admin.site.register(IntellectualPropertyChoice)
admin.site.register(Documentation)
admin.site.register(MoaChoice)

