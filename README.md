# Livraria Online

Um projeto de livraria online desenvolvido em Django, que permite aos usuários buscar livros, adicionar ao carrinho, finalizar compras e exportar o histórico de compras em PDF.

## Funcionalidades

- **Busca de Livros**: Integração com a API do Google Books para pesquisar livros por título, autor ou categoria.
- **Carrinho de Compras**: Adicione livros ao carrinho e veja o total antes de finalizar a compra.
- **Histórico de Compras**: Visualize suas compras anteriores.
- **Exportação de PDF**: Exporte seu histórico de compras para um arquivo PDF.

## Tecnologias Utilizadas

- Python
- Django
- PostgreSQL (ou MySQL)
- WeasyPrint (para geração de PDFs)

## Pré-requisitos

- Python 3.9 ou superior
- PostgreSQL ou MySQL
- pip (gerenciador de pacotes do Python)

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/livraria_online.git
   cd livraria_online
Crie e ative um ambiente virtual:

bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate  # Windows
Instale as dependências:

bash

pip install -r requirements.txt
Configure o banco de dados no arquivo settings.py:

Atualize as configurações de banco de dados com suas credenciais.
Faça as migrações:

bash

python manage.py migrate
Crie um superusuário (opcional, para acessar o admin):

bash

python manage.py createsuperuser
Inicie o servidor local:

bash

python manage.py runserver
Acesse a aplicação em seu navegador:

arduino

http://127.0.0.1:8000/
