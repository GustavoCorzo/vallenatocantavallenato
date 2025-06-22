from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from .models import CantoVallenato, Persona, AgrupacionMusical, AlbumVallenato, VersionVallenato, Role
from .forms import CantoVallenatoForm, FiltroCancionForm, AgrupacionMusicalForm, AlbumVallenatoForm, VersionVallenatoForm, FiltroVersionForm, PersonasPorRolForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'cantovallenato/canciones/home.html'

class CantaresView(TemplateView):
     template_name = 'cantovallenato/canciones/cantarvallenato.html'

class AgrupacionesView(TemplateView):
     template_name = 'cantovallenato/agrupaciones/agrupacionesvallenato.html'

class CreadoresView(TemplateView):
     template_name = 'cantovallenato/creadores/creadoresdelvallenato.html'

class RitmosView(TemplateView):
     template_name = 'cantovallenato/ritmos/ritmosdelvallenato.html'

class InstrumentosView(TemplateView):
     template_name = 'cantovallenato/instrumentos/instrumentosdelvallenato.html'

class CantoVallenatoCreateView(CreateView):
    model = CantoVallenato
    form_class = CantoVallenatoForm    
    template_name = 'cantovallenato/canciones/cantovallenato_form.html'
    context_object_name = 'canto'
    success_url = reverse_lazy('cantovallenato_list')

class CantoVallenatoListView(ListView):
    model = CantoVallenato
    template_name = 'cantovallenato/canciones/cantovallenato_list.html'
    context_object_name = 'cantos'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        compositor_id = self.request.GET.get('compositor')
        if compositor_id:
            queryset = queryset.filter(compositor_id=compositor_id)
        return queryset         
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FiltroCancionForm(self.request.GET or None)
        return context    
    
class CantoVallenatoUpdateView(UpdateView):
    model = CantoVallenato
    form_class = CantoVallenatoForm
    template_name = 'cantovallenato/canciones/actualizacanto_form.html'
    success_url = reverse_lazy('cantovallenato_list')

class CantoVallenatoDeleteView(DeleteView):
    model = CantoVallenato
    template_name = 'cantovallenato/canciones/cantovallenato_confirm_delete.html'
    success_url = reverse_lazy('cantovallenato_list')

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonasPorRolForm
    template_name = 'cantovallenato/creadores/personas_por_rol_form.html'

    
    def get_success_url(self):        
        rol_obj = self.object.roles.first()
        if rol_obj:
            return reverse_lazy('personas_por_rol', kwargs={'rol':rol_obj})
        else:
            # En caso de que no se haya asignado ningún rol, redirige a una página general o muestra mensaje
            return reverse_lazy('sin_rol_asignado') # Asegúrate de tener esta ruta o ajusta según tu estructura
class PersonaPorRolListView(ListView):
    model = Persona
    template_name = 'cantovallenato/creadores/personas_por_rol_list.html'
    context_object_name = 'personas' 

    def get_queryset(self):
        queryset = super().get_queryset()
        rol = self.kwargs.get('rol')
        if rol:
               queryset = queryset.filter(roles__name=rol)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rol'] = self.kwargs.get('rol')
        return context

class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'cantovallenato/creadores/persona_detail.html' 
    context_object_name = 'persona' 
            
class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonasPorRolForm
    template_name = 'cantovallenato/creadores/actualizacreador_form.html'
    success_url = reverse_lazy('cantarvallenato')
    def form_valid(self, form):
        if 'imagen' in form.changed_data:
            return super().form_valid(form)
        else:
            form.instance.imagen = self.object.imagen
        return super().form_valid(form)

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'cantovallenato/creadores/creador_confirm_delete.html'
    success_url = reverse_lazy('cantarvallenato')


class AgrupacionMusicalCreateView(CreateView):
    model = AgrupacionMusical
    form_class = AgrupacionMusicalForm    
    template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_form.html'
    success_url = reverse_lazy('agrupacionesvallenato_list')

class AgrupacionMusicalListView(ListView):
    model = AgrupacionMusical
    template_name = 'cantovallenato/agrupaciones/agrupacionesvallenato_list.html'
    context_object_name = 'agrupaciones'    

class AgrupacionMusicalDetailView(DetailView):
    model = AgrupacionMusical
    template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_detail.html'
    context_object_name = 'agrupacion'

class AgrupacionMusicalUpdateView(UpdateView):
    model = AgrupacionMusical
    form_class = AgrupacionMusicalForm
    template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_form.html'
    success_url = reverse_lazy('agrupacionesvallenato_list')

class AgrupacionMusicalDeleteView(DeleteView):
    model = AgrupacionMusical
    template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_confirm_delete.html'
    success_url = reverse_lazy('agrupacionesvallenato_list')


class AlbumVallenatoCreateView(CreateView):
    model = AlbumVallenato
    form_class = AlbumVallenatoForm    
    template_name = 'cantovallenato/albumes/albumvallenato_form.html'
    success_url = reverse_lazy('albumesvallenato_list')

class AlbumVallenatoListView(ListView):
    model = AlbumVallenato
    template_name = 'cantovallenato/albumes/albumesvallenato_list.html'
    context_object_name = 'albumes'    

class AlbumVallenatoDetailView(DetailView):
    model = AlbumVallenato
    template_name = 'cantovallenato/albumes/albumvallenato_detail.html'
    context_object_name = 'album'

class AlbumVallenatoUpdateView(UpdateView):
    model = AlbumVallenato
    form_class = VersionVallenatoForm
    template_name = 'cantovallenato/albumes/albumvallenato_form.html'
    success_url = reverse_lazy('albumesvallenato_list')

class AlbumVallenatoDeleteView(DeleteView):
    model = AlbumVallenato
    template_name = 'cantovallenato/albumes/albumvallenato_confirm_delete.html'
    success_url = reverse_lazy('albumesvallenato_list')


class VersionVallenatoCreateView(CreateView):
    model = VersionVallenato
    form_class = VersionVallenatoForm    
    template_name = 'cantovallenato/versiones/versionvallenato_form.html'
    success_url = reverse_lazy('versionesvallenato_list')

class VersionVallenatoListView(ListView):
    model = VersionVallenato
    template_name = 'cantovallenato/versiones/versionesvallenato_list.html'
    context_object_name = 'versiones' 

    def get_queryset(self):
        queryset = super().get_queryset()
        cancion = self.request.GET.get('cancion')
        if cancion:
            queryset = queryset.filter (cancion__id=cancion)
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FiltroVersionForm(self.request.GET or None)
        return context

class VersionVallenatoDetailView(DetailView):
    model = VersionVallenato
    template_name = 'cantovallenato/versiones/versionvallenato_detail.html'
    context_object_name = 'version'

class VersionVallenatoUpdateView(UpdateView):
    model = VersionVallenato
    form_class = VersionVallenatoForm
    template_name = 'cantovallenato/versiones/versionvallenato_form.html'
    success_url = reverse_lazy('versionesvallenato_list')

class VersionVallenatoDeleteView(DeleteView):
    model = VersionVallenato
    template_name = 'cantovallenato/versiones/versionvallenato_confirm_delete.html'
    success_url = reverse_lazy('versionesvallenato_list')

class SinRolAsignadoView(TemplateView):
    template_name = "cantovallenato/creadores/sin_rol_asignado.html"