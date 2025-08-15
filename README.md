SGE - Sistema de Gerenciamento de Estoque 📦
Um sistema web completo para gerenciamento de estoque, desenvolvido com Python e Django. A aplicação permite o controle total sobre produtos, incluindo o registro detalhado de entradas e saídas, fornecendo uma visão clara e organizada do inventário.

✨ Funcionalidades Principais
Dashboard Inteligente: Painel de controle com KPIs (Indicadores Chave de Desempenho), gráfico dos produtos com mais estoque e um feed de movimentações recentes.

CRUD Completo de Produtos: Cadastro, Leitura, Atualização e Deleção de produtos de forma intuitiva.

Controle de Movimentações: Registro detalhado de entradas e saídas para cada produto, atualizando o estoque em tempo real.

Autenticação Segura: Sistema de login para proteger o acesso aos dados do sistema.

Busca e Paginação: Funcionalidade de busca rápida por nome ou SKU e paginação para lidar com grandes volumes de dados de forma eficiente.

Feedback ao Usuário: Mensagens de sucesso e erro para todas as ações, melhorando a experiência de uso.

Interface Limpa e Responsiva: Design profissional com CSS organizado, garantindo uma boa experiência em desktops e dispositivos móveis.

Seeder de Dados: Comando para popular o banco de dados com 300 produtos a partir de um arquivo JSON, facilitando testes e demonstrações.

🛠️ Tecnologias Utilizadas
Backend: Python 3, Django

Frontend: HTML5, CSS3 (sem frameworks, apenas boas práticas)

Banco de Dados: SQLite 3 (padrão para desenvolvimento)

Geração de Dados: Faker

🚀 Como Executar o Projeto
Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

Pré-requisitos
Python 3.8+

Git

Passo a Passo
Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Crie e ative o ambiente virtual:

# Cria o ambiente
python -m venv venv

# Ativa no Windows
.\venv\Scripts\activate

# Ativa no Linux/macOS
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

(Nota: Se você não tiver um requirements.txt, crie um com pip freeze > requirements.txt)

Aplique as migrações do banco de dados:

python manage.py migrate

Crie um superusuário para acessar o sistema:

python manage.py createsuperuser

(Siga as instruções para definir nome de usuário, email e senha)

(Opcional) Popule o banco de dados com dados de teste:
Primeiro, gere o arquivo JSON:

python gerar_json.py

Depois, execute o seeder:

python manage.py seed_products

Inicie o servidor de desenvolvimento:

python manage.py runserver

Acesse a aplicação no seu navegador:
http://127.0.0.1:8000/

📖 Uso
Após iniciar a aplicação, acesse a URL e faça login com as credenciais do superusuário que você criou. Você será direcionado ao Dashboard e poderá começar a explorar as funcionalidades, como cadastrar novos produtos e registrar movimentações.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido com ❤️ por Seu Nome