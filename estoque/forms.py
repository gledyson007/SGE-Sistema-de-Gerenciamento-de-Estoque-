from django import forms
from .models import Produto, MovimentacaoEstoque

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome', 
            'sku', 
            'descricao', 
            'preco_custo', 
            'preco_venda',   
            'unidade_medida'    
        ]

class MovimentacaoEstoqueForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ['quantidade', 'observacao']