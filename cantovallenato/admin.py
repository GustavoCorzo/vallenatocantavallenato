from django.contrib import admin
from .models import CantoVallenato,  RitmoVallenato, VersionVallenato, AlbumVallenato,  AgrupacionMusical, Persona, Role

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre_artistico',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(RitmoVallenato)
class RitmoVallenataAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(CantoVallenato)
class CantoVallenatoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'compositor', 'ritmo',)

@admin.register(AgrupacionMusical)
class AgrupacionMusicalAdmin(admin.ModelAdmin):
    list_display = ('razon_social',)

@admin.register(AlbumVallenato)
class AlbumVallenatoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'agrupacion', 'anio_graba', 'isbn',)

@admin.register(VersionVallenato)
class VersionVallenatoAdmin(admin.ModelAdmin):
    list_display = ('cancion', 'album',)

