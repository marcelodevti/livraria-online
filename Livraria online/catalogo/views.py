import requests
from django.shortcuts import render
from .models import Livro

def buscar_livros(request):
    query = request.GET.get('q', '')
    if query:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
        response = requests.get(url)
        dados = response.json()

        livros = []
        for item in dados.get('items', []):
            info = item['volumeInfo']
            livros.append({
                'titulo': info.get('title'),
                'autor': ', '.join(info.get('authors', [])),
                'descricao': info.get('description', ''),
                'isbn': info.get('industryIdentifiers', [{}])[0].get('identifier', ''),
                'imagem_capa': info.get('imageLinks', {}).get('thumbnail', ''),
            })

        return render(request, 'catalogo/buscar_livros.html', {'livros': livros})
    return render(request, 'catalogo/buscar_livros.html')

from django.shortcuts import get_object_or_404, redirect
from .models import Carrinho, Livro, ItemCarrinho

def adicionar_ao_carrinho(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user, completed=False)
    item, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, livro=livro)
    if not created:
        item.quantidade += 1
        item.save()
    return redirect('ver_carrinho')

def ver_carrinho(request):
    carrinho = Carrinho.objects.get(usuario=request.user)
    return render(request, 'catalogo/ver_carrinho.html', {'carrinho': carrinho})

from django.shortcuts import redirect

def finalizar_compra(request):
    carrinho = Carrinho.objects.get(usuario=request.user)
    for item in carrinho.itemcarrinho_set.all():
        Compra.objects.create(
            usuario=request.user,
            livro=item.livro,
            quantidade=item.quantidade
        )
    carrinho.delete()  # Limpa o carrinho após a compra
    return redirect('historico_compras')

from django.shortcuts import render
from .models import Compra
from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse

# View para exibir o histórico de compras
def historico_compras(request):
    compras = Compra.objects.filter(usuario=request.user)
    return render(request, 'catalogo/historico_compras.html', {'compras': compras})

# View para exportar o histórico de compras como PDF
def exportar_historico_pdf(request):
    compras = Compra.objects.filter(usuario=request.user)
    html_string = render_to_string('catalogo/historico_compras_pdf.html', {'compras': compras})
    html = HTML(string=html_string)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="historico_compras.pdf"'
    html.write_pdf(response)

    return response
