"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from management.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^project/new/$', projectFormView.as_view(), name= 'projectForms'),
    url(r'^plan/new/$', PlanFormView.as_view(), name= 'planForm'),
    url(r'^scientificactivity/new/$',ScientificActivityCreateView.as_view(),name='createAcientificActivity'),
    url(r'^scientificactivity/update/(?P<pk>\d+)/$',ScientificActivityUpdateView.as_view(),name='updateScientificActivity'),
    url(r'^scientificactivity/delete/(?P<pk>\d+)/$', ScientificActivityDeleteView.as_view(),name='deleteScientificActivity'),
    url(r'^plan/update/(?P<pk>\d+)/$', PlanFormUpdateView.as_view(), name= 'planFormUpdate'),
    url(r'^plan/delete/(?P<pk>\d+)/$', PlanFormDeleteView.as_view(), name= 'planFormDelete'),
    url(r'^scientificarea/new/$', ScientificAreaCreateView.as_view(), name='createAreaActivity'),
    url(r'^documentation/new/$', DocumentationView.as_view(), name='createDocumentation'),
    url(r'^scientificarea/update/(?P<pk>\d+)/$',ScientificAreaUpdateView.as_view(),name='updateScientificArea'),
    url(r'^scientificarea/delete/(?P<pk>\d+)/$', ScientificAreaDeleteView.as_view(),name='deleteScientificArea'),
    url(r'^documentation/delete/(?P<pk>\d+)/$', DocumentationDeleteView.as_view(), name='documentationFormDelete'),
]
