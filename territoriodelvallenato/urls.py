from django.urls import path
from . views import TerritorioView

urlpatterns = [
    path("territorio/", TerritorioView.as_view(), name="territorio")
]
