from django.urls import path
from . views import FestivalesView


urlpatterns = [
    path('festivales/', FestivalesView.as_view(), name='festivales'),
  
]