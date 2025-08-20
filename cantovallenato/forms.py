from crispy_forms.helper import FormHelper
from django import forms
from .models import CantoVallenato, AgrupacionMusical, AlbumVallenato, VersionVallenato, Role, Persona

class CantoVallenatoForm(forms.ModelForm):
    class Meta:
        model = CantoVallenato
        fields = ['titulo', 'compositor', 'ritmo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input border border-gray-300 rounded-md',}), 
            'compositor': forms.Select(attrs={'placeholder' : 'Compositor', 'class': 'form-input border border-gray-300 rounded-md',}), 
            'ritmo': forms.Select(attrs={'placeholder' : 'Ritmo', 'class': 'form-input border border-gray-300 rounded-md',})}

class FiltroCancionForm(forms.ModelForm):
    compositor = forms.ModelChoiceField(queryset=Persona.objects.filter(roles__name=Role.COMPOSITOR), required=False)

    class Meta:
        model = CantoVallenato
        fields = ['compositor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input border border-gray-300 rounded-md',}), 
            'compositor': forms.TextInput(attrs={'placeholder' : 'Compositor', 'class': 'form-input border border-gray-300 rounded-md',}), 
            'ritmo': forms.TextInput(attrs={'placeholder' : 'Ritmo', 'class': 'form-input border border-gray-300 rounded-md',})}
        
class AbstractPersonaForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(), 
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=True, 
        label='Roles'                                
    )

    class Meta:
        model = Persona     
        fields = '__all__'
        
       # ['nombres', 'apellidos', 'formacion_academica', 'nombre_artistico', 'anio_nace', 'lugar_nace', 'lugar_muere', 'imagen', 'roles']

class PersonasPorRolForm(AbstractPersonaForm):
    class Meta(AbstractPersonaForm.Meta):
        model = Persona
        fields = ['nombres', 'apellidos', 'formacion_academica', 'nombre_artistico', 'anio_nace', 'lugar_nace', 'lugar_muere', 'imagen', 'roles']

def save(self, *args, **kwargs):
    if not self.cleaned_data.get['imagen']:
        raise forms.ValidationError("La imagen es obligatoria.")
    return super().save(*args, **kwargs)


class AgrupacionMusicalForm(forms.ModelForm):
    class Meta:
        model = AgrupacionMusical
        fields = ['razon_social', 'acordeonero', 'voz_principal', 'corista_uno', 'corista_dos', 'cajero', 'guacharaquero', 'guitarrista']

class AlbumVallenatoForm(forms.ModelForm):
    #cancion = forms.ModelChoiceField( queryset=CantoVallenato.objects.all(), required=True, label='Canción', widget=forms.Select(attrs={'class': 'form-control'}) )

    class Meta:
        model = AlbumVallenato
        fields = ['titulo', 'agrupacion', 'anio_graba', 'isbn']
        
    #def __init__(self, *args, **kwargs):
        #super().__init__ (*args, **kwargs)
        #self.fields['cancion'].label_from_instance = lambda obj: obj.titulo

class VersionVallenatoForm(forms.ModelForm):
    cancion = forms.ModelChoiceField( queryset=CantoVallenato.objects.all(), required=True, label='Canción', widget=forms.Select(attrs={'class': 'form-control'}) )

    class Meta:
        model = VersionVallenato
        fields = ['cancion', 'album', 'interprete']

    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        self.fields['cancion'].label_from_instance = lambda obj: obj.titulo
        self.fields['album'].label_from_instance = lambda obj: obj.titulo 
        self.fields['interprete'].label_from_instance = lambda obj: obj.razon_social  

class FiltroVersionForm(forms.ModelForm):
    cancion = forms.ModelChoiceField(queryset=CantoVallenato.objects.all(), required=False)

    class Meta:
        model = VersionVallenato
        fields = ['cancion']
        widgets = {
            'cancion': forms.TextInput(attrs={'class': 'form-input border border-gray-300 rounded-md',}), 
            'album': forms.TextInput(attrs={'placeholder' : 'Album', 'class': 'form-input border border-gray-300 rounded-md',}),
            'agrupacion': forms.TextInput(attrs={'placeholder' : 'Agrupacion','class':'form-input border border-gray-300 rounded-md',})                       
        }

    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        self.fields['cancion'].label_from_instance = lambda obj: obj.titulo
    