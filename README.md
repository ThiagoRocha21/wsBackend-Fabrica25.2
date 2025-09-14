# wsBackend-Fabrica25.2

Desafio da Fábrica de Software 25.2: Projeto Django com as entidades **Receitas** e **Categoria**, incluindo funcionalidades completas de CRUD.

## 🚀 Começando

Este guia vai te ajudar a configurar o projeto localmente para desenvolvimento e testes.

Veja a seção **[Implantação](#-implantação)** para informações sobre colocar o projeto em produção.

### 📋 Pré-requisitos

- Python 3.8+  
- pip  
- Virtualenv (recomendado)  
- Git (para clonar o repositório)  

### 🔧 Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/wsBackend-Fabrica25.2.git
    cd wsBackend-Fabrica25.2
    ```

2. Crie e ative ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

6. Rode o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

7. Abra no navegador:
    ```
    http://127.0.0.1:8000/
    ```

### 🎉 Funcionalidades principais

- CRUD completo para **Receitas** e gerenciamento de suas categorias.  
- Tela para adicionar e editar receitas com formulário amigável (usando crispy forms).  
- Visualização das receitas cadastradas com ações de atualizar e excluir.  
- Confirmação antes de excluir uma receita.  
- Integração com API externa para buscar receitas de massa (`/receitas-externas/`).


### 🛠️ Construído com
 - Django
 - Framework web
Bootstrap 4
 - Front-end responsivo
django-crispy-forms
 - Formulários estilizados
requests
 - Consumo de API externa
