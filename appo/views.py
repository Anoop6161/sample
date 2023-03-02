from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

class aboutview(TemplateView):
    template_name = ('about.html')

class HomeView(TemplateView):
    template_name = ('home.html')


# Create your views here.
