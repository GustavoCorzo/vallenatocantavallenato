from django.urls import path
from . views import PromotoresView

urlpatterns = [
    path('promotores/', PromotoresView.as_view(), name='promotores'),
  
]