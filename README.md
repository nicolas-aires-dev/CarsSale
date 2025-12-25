# CarsSale 🚗

Sistema de cadastro de carros à venda, desenvolvido em **Python/Django** com integração de **IA** para geração automática de descrições dos veículos.

## ✨ Funcionalidades
- CRUD completo de veículos (marca, modelo, ano, etc).
- Integração com **API da OpenAI** para gerar descrições automáticas de venda em até 250 caracteres.
- Persistência dos dados em banco relacional (**PostgreSQL**).
- Estrutura preparada para deploy com **uWSGI + Nginx** (testado em AWS EC2).

## 🛠️ Tecnologias utilizadas
- Python 3.x
- Django 
- OpenAI API (`openai==1.66.3`)
- SQL Server
- uWSGI / Nginx
- Docker (opcional)
- GitHub Actions (para CI/CD futuramente)

## 🚀 Como rodar localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com/nicolas-aires-dev/CarsSale.git
   cd CarsSale
   
2. Crie e ative um ambiente virtual:

   ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    ./venv/Scripts/Activate.ps1      # Windows

3. Instale as dependências:

   ```bash
    pip install -r requirements.txt

4. Configure sua chave da OpenAI em um arquivo .env:

   ```bash
    OPENAI_API_KEY=your_api_key_here

   
5. Execute o servidor:

   ```bash
    python manage.py runserver

# 📦 Estrutura do projeto

    ```bash
    CarsSale/
    │── src/              # Código principal
    │── media/cars/       # Diretório de imagens (ignorado no Git)
    │── migrations/       # Controle de banco de dados
    │── uwsgi.ini.example # Configuração genérica para deploy
    │── requirements.txt  # Dependências
    │── README.md         # Documentação
    
# 🌐 Deploy
- Projeto testado em AWS EC2 com uWSGI + Nginx.
- Configurações sensíveis foram removidas do repositório.

# 📌 Diferenciais
- Uso prático de IA generativa em um CRUD real.
- Experiência com integração de APIs e deploy em nuvem.
- Estudo contínuo de LangChain para expandir funcionalidades.

# 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.