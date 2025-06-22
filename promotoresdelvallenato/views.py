from django.shortcuts import render
from django.views.generic import TemplateView

class PromotoresView(TemplateView):
     template_name = 'promotoresdelvallenato/promotores.html'