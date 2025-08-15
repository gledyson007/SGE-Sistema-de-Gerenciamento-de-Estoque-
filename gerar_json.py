import json
import random
from faker import Faker

# Inicializa o Faker para gerar dados em português
fake = Faker('pt_BR')

lista_produtos = []

# Gera 300 produtos
for i in range(300):
    # Gera um nome de produto mais realista (combinação de adjetivo + substantivo)
    nome_produto = f"{fake.word().capitalize()} {fake.word().capitalize()}"
    
    produto = {
        "nome": nome_produto,
        "sku": fake.unique.ean(length=13), # CORREÇÃO APLICADA AQUI
        "descricao": fake.text(max_nb_chars=250),
        "preco_custo": round(random.uniform(5.0, 250.0), 2),
        "preco_venda": round(random.uniform(25.0, 499.0), 2),
        "quantidade": random.randint(0, 200),
        "unidade_medida": random.choice(['unidade', 'caixa', 'pacote', 'kg'])
    }
    lista_produtos.append(produto)

# Salva a lista de produtos em um arquivo JSON
# indent=4 formata o arquivo para ser mais legível
with open('produtos.json', 'w', encoding='utf-8') as f:
    json.dump(lista_produtos, f, indent=4, ensure_ascii=False)

print("Arquivo 'produtos.json' com 300 produtos foi criado com sucesso!")
