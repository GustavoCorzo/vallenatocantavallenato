from django.urls import path
from . views import CulturaView

urlpatterns = [
    path('cultura/', CulturaView.as_view(), name='cultura'),
  
]