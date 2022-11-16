from django.contrib import admin
from .models import Receita

# Register your models here.
# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

# listando as receitas no admin
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',) # como pesquisar
    list_filter = ('categoria',) # filtros
    list_editable = ('publicada',)
    list_per_page = 10 # paginação



admin.site.register(Receita, ListandoReceitas)