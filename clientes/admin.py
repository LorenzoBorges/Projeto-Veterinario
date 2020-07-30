from django.contrib import admin
from . import models

class VacinaInline(admin.TabularInline):
    model = models.Vacina
    extra = 1

class ConsultaInline(admin.TabularInline):
    model = models.Consulta
    extra = 1

class CirurgiaInline(admin.TabularInline):
    model = models.Cirurgia
    extra = 1

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'raca', 'dono', 'plano', 'mostrar')
    list_display_links = ('id', 'animal', 'dono')
    list_per_page = 10
    search_fields = ('animal',)
    list_editable = ('mostrar',)
    inlines = [
        VacinaInline,
        ConsultaInline,
        CirurgiaInline,
    ]


admin.site.register(models.Plano)
admin.site.register(models.Dono)
admin.site.register(models.Animal, AnimalAdmin)
admin.site.register(models.Vacina)
admin.site.register(models.Consulta)
admin.site.register(models.Cirurgia)