import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from estoque.models import Produto

class Command(BaseCommand):
    help = 'Popula o banco de dados com produtos a partir de um arquivo JSON'

    def handle(self, *args, **kwargs):
        # Limpa os produtos existentes
        self.stdout.write('Limpando produtos existentes...')
        Produto.objects.all().delete()

        # Constrói o caminho para o arquivo JSON na raiz do projeto
        json_file_path = os.path.join(settings.BASE_DIR, 'produtos.json')

        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                produtos_data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Arquivo "produtos.json" não encontrado. Rode o script "gerar_json.py" primeiro.'))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Erro ao decodificar o arquivo JSON. Verifique se o arquivo está formatado corretamente.'))
            return

        produtos_para_criar = []
        for data in produtos_data:
            produto = Produto(
                nome=data['nome'],
                sku=data['sku'],
                descricao=data['descricao'],
                preco_custo=data['preco_custo'],
                preco_venda=data['preco_venda'],
                quantidade=data['quantidade'],
                unidade_medida=data['unidade_medida']
            )
            produtos_para_criar.append(produto)
        
        # Usa bulk_create para inserir todos os produtos de uma vez
        Produto.objects.bulk_create(produtos_para_criar)

        self.stdout.write(self.style.SUCCESS(f'>> {len(produtos_para_criar)} produtos foram importados do JSON com sucesso!'))
