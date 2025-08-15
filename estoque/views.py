from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Produto, MovimentacaoEstoque
from .forms import ProdutoForm, MovimentacaoEstoqueForm
from django.db.models import Sum, F

@login_required
def dashboard_view(request):
    # KPIs existentes
    total_produtos = Produto.objects.count()
    valor_total_estoque_obj = Produto.objects.aggregate(total=Sum(F('quantidade') * F('preco_custo')))
    valor_total_estoque = valor_total_estoque_obj['total'] or 0

    # Novos KPIs
    total_itens_estoque = Produto.objects.aggregate(total=Sum('quantidade'))['total'] or 0
    produtos_sem_estoque = Produto.objects.filter(quantidade=0).count()
    produtos_estoque_baixo = Produto.objects.filter(quantidade__gt=0, quantidade__lte=10).count()

    # Movimentações Recentes (últimas 5)
    movimentacoes_recentes = MovimentacaoEstoque.objects.order_by('-data_movimentacao')[:5]

    # Dados para o Gráfico
    produtos_mais_estoque = Produto.objects.order_by('-quantidade')[:5]

    context = {
        'total_produtos': total_produtos,
        'valor_total_estoque': valor_total_estoque,
        'total_itens_estoque': total_itens_estoque,
        'produtos_sem_estoque': produtos_sem_estoque,
        'produtos_estoque_baixo': produtos_estoque_baixo,
        'movimentacoes_recentes': movimentacoes_recentes,
        'produtos_mais_estoque': produtos_mais_estoque,
    }

    return render(request, 'estoque/dashboard.html', context)
@login_required
def lista_produtos_view(request):
    query = request.GET.get('q')
    if query:
        produto_list = Produto.objects.filter(
            Q(nome__icontains=query) | Q(sku__icontains=query)
        ).order_by('nome')
    else:
        produto_list = Produto.objects.all().order_by('nome')

    paginator = Paginator(produto_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'estoque/lista_produtos.html', context)

@login_required
def cria_produto_view(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produdos')
    else:
        form = ProdutoForm()
    
    context = {'form': form}
    return render(request, 'estoque/cria_produto.html', context)

@login_required
def editar_produto_view(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    
    else:
        form = ProdutoForm(instance=produto)

    context = {
        'form': form,
        'produto': produto,
    }
    return render(request, 'estoque/edita_produto.html', context)

@login_required
def deletar_produto_view(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    
    context = {
        'produto': produto
    }
    return render(request, 'estoque/deleta_produto.html', context)

@login_required
def detalhe_produto_view(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    movimentacoes = produto.movimentacoes.all()
    context = {
        'produto': produto,
        'movimentacoes': movimentacoes,
    }
    return render(request, 'estoque/detalhe_produto.html', context)

@login_required
def cria_movimentacao_view(request, pk, tipo):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        form = MovimentacaoEstoqueForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.produto = produto
            movimentacao.usuario = request.user
            movimentacao.tipo = tipo

            if tipo == 'ENTRADA':
                produto.quantidade += movimentacao.quantidade
            elif tipo == 'SAIDA':
                if produto.quantidade >= movimentacao.quantidade:
                    produto.quantidade -= movimentacao.quantidade
            else:
                form.add_error('quantidade', 'Estoque insuficiente para esta saída')
                context = {'form': form, 'produto': produto, 'tipo': tipo}
                return render(request, 'estoque/cria_movimentacao.html', context)
            
            produto.save()
            movimentacao.save()

            return redirect('detalhe_produto', pk=produto.pk)
    else:
        form = MovimentacaoEstoqueForm

    context = {
        'form': form,
        'produto': produto,
        'tipo': tipo
    }
    return render(request, 'estoque/cria_movimentacao.html', context)
