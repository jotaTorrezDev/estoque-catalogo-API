# Core API

Uma API REST em Django para gerenciar produtos, categorias e pedidos.

## Sugestões de nome para o repositório GitHub

- `core-api`
- `django-store-api`
- `estoque-catalogo-api`
- `api-produtos-pedidos`
- `django-pedidos-api`

Escolha um nome simples e descritivo; por exemplo, `core-api` ou `estoque-catalogo-api` funcionam bem.

## Visão geral do projeto

Este projeto é uma aplicação Django com Django REST Framework que oferece endpoints para:

- CRUD de categorias (`Categoria`)
- CRUD de produtos (`Produto`)
- CRUD de pedidos (`Pedidos`)

A aplicação está configurada para usar autenticação por token e um banco de dados SQLite.

## Estrutura principal

- `rdf/` - projeto Django principal
- `core/` - app Django com modelos, serializers, views e rotas
- `db.sqlite3` - banco de dados SQLite local
- `requeriments.txt` - dependências do Python

## Dependências

As dependências ficam em `requeriments.txt`. O projeto usa pelo menos:

- Django
- djangorestframework
- djangorestframework-authtoken

## Como rodar localmente

1. Crie e ative um ambiente virtual:

```powershell
python -m venv venv
venv\Scripts\Activate
```

2. Instale as dependências:

```powershell
pip install -r requeriments.txt
```

3. Aplique as migrations:

```powershell
python manage.py migrate
```

4. Crie um usuário administrador (opcional, mas recomendado):

```powershell
python manage.py createsuperuser
```

5. Inicie o servidor:

```powershell
python manage.py runserver
```

## Endpoints principais

- `POST /api/token/` - obter token de autenticação
- `GET /api/categorias/` - listar categorias
- `GET /api/produtos/` - listar produtos
- `GET /api/pedidos/` - listar pedidos

Também existem endpoints para criar, atualizar e excluir recursos via rotas padrões do DRF.

## Autenticação

A API exige token para acesso. Use o token no cabeçalho:

```
Authorization: Token <seu-token>
```

## Observações

- O projeto atualmente usa `DEBUG = True`, adequado para desenvolvimento.
- O banco de dados padrão é SQLite (`db.sqlite3`).
- Ajustes nos serializers e nos modelos podem ser necessários caso novos campos sejam adicionados.

---

Se desejar, posso também ajudar a organizar o repositório com um `.gitignore` e nomear o projeto para publicação no GitHub.