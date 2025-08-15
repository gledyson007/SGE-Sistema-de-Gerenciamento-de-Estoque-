from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('produtos/', views.lista_produtos_view, name='lista_produtos'),
    path('produtos/novo/', views.cria_produto_view, name='cria_produto'),
    path('produtos/<int:pk>/editar/', views.editar_produto_view, name='edita_produto'),
    path('produtos/<int:pk>/deletar/', views.deletar_produto_view, name='deleta_produto'),
    path('produtos/<int:pk>/', views.detalhe_produto_view, name='detalhe_produto'),
    path('produtos/<int:pk>/movimentacao/entrada/', views.cria_movimentacao_view, {'tipo': 'ENTRADA'}, name='movimentacao_entrada'),
    path('produtos/<int:pk>/movimentacao/saida/', views.cria_movimentacao_view, {'tipo': 'SAIDA'}, name='movimentacao_saida'),

]
