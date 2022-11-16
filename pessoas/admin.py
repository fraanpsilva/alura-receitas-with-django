from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',) # como pesquisar
    list_per_page = 10 # paginação

admin.site.register(Pessoa, ListandoPessoas)