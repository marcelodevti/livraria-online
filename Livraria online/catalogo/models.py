from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    isbn = models.CharField(max_length=13, unique=True)
    imagem_capa = models.URLField()

    def __str__(self):
        return self.titulo

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)
    quantidade = models.PositiveIntegerField()

    def total(self):
        return self.quantidade * self.livro.preco

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    livros = models.ManyToManyField(Livro, through='ItemCarrinho')

class ItemCarrinho(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
