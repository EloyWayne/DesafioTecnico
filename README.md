markdown
Copiar código
# Desafio Técnico

## Descrição do Projeto

Este projeto é uma aplicação desenvolvida em Django com o objetivo de realizar scraping de dados das Olimpíadas e fornecer uma API REST para consultar informações sobre medalhas por país e esporte.

## Requisitos

Antes de começar, certifique-se de ter os seguintes softwares instalados:

* Python 3.12 ou superior
* Git
* Virtualenv (opcional, mas recomendado)

## Passos para Configuração

### 1. Clonar o Repositório

Clone o repositório para o seu ambiente local:

       ```sh
       git clone https://github.com/EloyWayne/DesafioTecnico.git
       cd DesafioTecnico
2. Criar e Ativar o Ambiente Virtual
Crie um ambiente virtual para isolar as dependências do projeto:

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

Windows:

bash
Copiar código
venv\Scripts\activate
macOS/Linux:

bash
Copiar código
source venv/bin/activate
3. Instalar as Dependências
Instale todas as dependências do projeto usando o arquivo requirements.txt:

bash
Copiar código
pip install -r requirements.txt
4. Configurar o Banco de Dados
Realize as migrações para configurar o banco de dados SQLite que acompanha o Django:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
5. Executar o Scraping
Execute o script de scraping para popular o banco de dados com os dados das medalhas olímpicas:

bash
Copiar código
python manage.py shell
No shell do Django, execute:

python
Copiar código
from apps.medals.scraper import fetch_medal_data
fetch_medal_data()
6. Iniciar o Servidor
Após configurar o banco de dados, inicie o servidor de desenvolvimento:

bash
Copiar código
python manage.py runserver
A aplicação estará disponível em http://127.0.0.1:8000/.

7. Acessar a API
Os endpoints da API estão configurados com o Django REST Framework. Você pode acessar os seguintes endpoints:

Lista de Países com Medalhas: http://127.0.0.1:8000/Country/
Lista de Esportes: http://127.0.0.1:8000/Sport/
Lista de Medalhas: http://127.0.0.1:8000/Medal/
8. Acesso à Administração do Django
Para acessar o painel administrativo do Django:

bash
Copiar código
python manage.py createsuperuser
Depois, acesse http://127.0.0.1:8000/admin/ e faça login com as credenciais criadas.


       
      


