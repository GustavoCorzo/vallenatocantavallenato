from django.shortcuts import render
from django.views.generic import TemplateView

class FestivalesView(TemplateView):
     template_name = 'festivalesdelvallenato/festivales.html'
