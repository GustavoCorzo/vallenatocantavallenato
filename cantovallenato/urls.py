from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cantovallenato.views import HomePageView, CantaresView, CantoVallenatoCreateView, CantoVallenatoListView, CantoVallenatoUpdateView, CantoVallenatoDeleteView, PersonaCreateView, PersonaPorRolListView, PersonaDetailView, PersonaUpdateView, PersonaDeleteView,AgrupacionMusicalCreateView, AgrupacionMusicalListView, AgrupacionMusicalDetailView, AgrupacionMusicalUpdateView, AgrupacionMusicalDeleteView, AlbumVallenatoCreateView, AlbumVallenatoListView, AlbumVallenatoDetailView, AlbumVallenatoUpdateView, AlbumVallenatoDeleteView, VersionVallenatoCreateView, VersionVallenatoListView, VersionVallenatoDetailView, VersionVallenatoUpdateView, VersionVallenatoDeleteView, SinRolAsignadoView, AgrupacionesView

urlpatterns = [
path('', HomePageView.as_view(), name='cantovallenato/canciones/home'),
path('cantares/', CantaresView.as_view(), name='cantarvallenato'),
path('canto/', CantoVallenatoCreateView.as_view(), name='cantovallenato_create'),
path('cantos/', CantoVallenatoListView.as_view(), name='cantovallenato_list'),
path('canto/<int:pk>/edit/', CantoVallenatoUpdateView.as_view(), name='cantovallenato_edit'),
path('canto/<int:pk>/delete/', CantoVallenatoDeleteView.as_view(), name='cantovallenato_delete'),

path('persona/', PersonaCreateView.as_view(), name='persona_create'),
path('personas/<str:rol>/', PersonaPorRolListView.as_view(), name='personas_por_rol'),
path('persona/<int:pk>/', PersonaDetailView.as_view(), name='persona_detail'),
path("persona/<int:pk>/edit", PersonaUpdateView.as_view(), name="persona_edit"),
path("persona/<int:pk>/delete", PersonaDeleteView.as_view(), name="persona_delete"),


#path('conjuntos/', AgrupacionesView.as_view(), name='agrupacionesvallenato'),

path('agrupacion/', AgrupacionMusicalCreateView.as_view(), name='agrupacionvallenato_create'),
path('agrupaciones/', AgrupacionMusicalListView.as_view(), name='agrupacionesvallenato_list'),
path('agrupacion/<int:pk>/', AgrupacionMusicalDetailView.as_view(), name='agrupacionvallenato_detail'),
path('agrupacion/<int:pk>/edit/', AgrupacionMusicalUpdateView.as_view(), name='agrupacionvallenato_edit'),
path('agrupacion/<int:pk>/delete/', AgrupacionMusicalDeleteView.as_view(), name='agrupacionvallenato_delete'),

path('album/', AlbumVallenatoCreateView.as_view(), name='albumvallenato_create'),
path('albumes/', AlbumVallenatoListView.as_view(), name='albumesvallenato_list'),
path('album/<int:pk>/', AlbumVallenatoDetailView.as_view(), name='albumvallenato_detail'),
path('album/<int:pk>/edit/', AlbumVallenatoUpdateView.as_view(), name='albumvallenato_edit'),
path('album/<int:pk>/delete/', AlbumVallenatoDeleteView.as_view(), name='albumvallenato_delete'),

path('version/', VersionVallenatoCreateView.as_view(), name='versionvallenato_create'),
path('versiones/', VersionVallenatoListView.as_view(), name='versionesvallenato_list'),
path('version/<uuid:pk>/', VersionVallenatoDetailView.as_view(), name='versionvallenato_detail'),
path('version/<uuid:pk>/edit/', VersionVallenatoUpdateView.as_view(), name='versionvallenato_edit'),
path('version/<uuid:pk>/delete/', VersionVallenatoDeleteView.as_view(), name='versionvallenato_delete'),

path("sin-rol/", SinRolAsignadoView.as_view(), name="sin_rol_asignado"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
