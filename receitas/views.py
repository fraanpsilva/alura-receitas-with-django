from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita


def index(request):
    # pegando os dados do banco - filtrando e mostrando
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    dados = {
        'receitas' : receitas
    }
    return render( request,'index.html', dados)

def receita(request, receita_id):
    # pegando parametros da url
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    return render (request, 'receita.html', receita_a_exibir)

def buscar(request):
    # buscando todas as receitas
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    # exibindo as receitas a partir da busca
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar'] # pegando o conteúdo da requisição
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar) # verificando se há alguma receita com a palavra buscada

    dados = {
        'receita': lista_receitas
    }
    return render(request, 'buscar.html', dados)
