from django.shortcuts import render
from django.views.generic import TemplateView

class CulturaView(TemplateView):
     template_name = 'culturadelvallenato/cultura.html'

