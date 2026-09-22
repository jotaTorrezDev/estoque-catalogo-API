# Estoque & Catálogo API

API REST em Django para gerenciamento de categorias, produtos e pedidos, com autenticação por token.

## Tecnologias

- Python, Django, Django REST Framework
- Autenticação por Token
- SQLite (desenvolvimento) / PostgreSQL (produção)

## Estrutura principal

- `rdf/` — projeto Django principal (settings, urls)
- `core/` — app com modelos, serializers, views e rotas
- `requirements.txt` — dependências do projeto

## Como rodar localmente

1. Crie e ative um ambiente virtual:

```powershell
python -m venv venv
venv\Scripts\Activate
```

2. Instale as dependências:

```powershell
pip install -r requirements.txt
```

3. Crie um arquivo `.env` na raiz do projeto com:
4. Aplique as migrations:

```powershell
python manage.py migrate
```

5. Crie um usuário administrador:

```powershell
python manage.py createsuperuser
```

6. Inicie o servidor:

```powershell
python manage.py runserver
```

## Endpoints principais

- `POST /api/token/` — obter token de autenticação
- `GET /api/categorias/` — listar categorias
- `GET /api/produtos/` — listar produtos
- `GET /api/pedidos/` — listar pedidos

Também existem rotas para criar, atualizar e excluir cada um desses recursos, seguindo o padrão do DRF.

## Autenticação

A API exige token para acesso. Envie o token no cabeçalho das requisições:

## Documentação interativa

Disponível em `/api/docs/`, com a lista de todos os endpoints e a opção de testar cada um diretamente pelo navegador.

## Observações

- Em produção, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` e a conexão com o banco são lidos de variáveis de ambiente.
- Ajustes nos serializers e modelos podem ser necessários ao adicionar novos campos.
