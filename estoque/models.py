from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Produto")
    sku = models.CharField(max_length=100, unique=True, verbose_name="SKU")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Venda")
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Venda")
    quantidade = models.PositiveIntegerField(default=0, verbose_name="Quantidade em Estoque")
    unidade_medida = models.CharField(max_length=20, default='unidade', verbose_name="Unidade de Medida")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.sku})"
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']

class MovimentacaoEstoque(models.Model):
    TIPO_MOVIMENTACAO = [
        ("ENTRADA", "Entrada"),
        ("SAIDA", "Saida")
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='movimentacoes')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMENTACAO, verbose_name="Tipo da Movimentação")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade Movimentada")
    data_movimentacao = models.DateTimeField(default=timezone.now, verbose_name="Data da Movimentação")
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return f"{self.get_tipo_display()} de {self.quantidade}x {self.produto.nome}"
    
    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
        ordering = ['-data_movimentacao']
