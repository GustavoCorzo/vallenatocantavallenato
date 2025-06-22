from django.shortcuts import render
from django.views.generic import TemplateView

class TerritorioView(TemplateView):
     template_name = 'territoriodelvallenato/territorio.html'
