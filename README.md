# 📊 GitHub Trend Analyzer - Java Ecosystem

Um pipeline de Engenharia de Dados (ETL) ponta a ponta que extrai, transforma, armazena e visualiza métricas dos repositórios Java mais populares do GitHub.

O objetivo deste projeto é ir além do simples número de "Estrelas" e calcular métricas reais de **Engajamento** e **Taxa de Contribuição** das comunidades de software open-source.

---

## 🏗️ Arquitetura do Projeto

O projeto foi construído utilizando uma arquitetura modularizada:

1. **Extract:** Consumo da API REST do GitHub para buscar os repositórios Java mais bem avaliados.
2. **Transform:** Limpeza de dados, tipagem e criação de métricas derivadas (Engajamento e Contribuição) utilizando **Pandas**.
3. **Load:** Carga dos dados em um banco de dados relacional **PostgreSQL** rodando em **Docker**, utilizando SQLAlchemy e lógica de _Upsert_ para evitar duplicidade.
4. **Visualize:** Um Dashboard interativo construído com **Streamlit** e **Plotly** para exploração visual dos dados.

---

## 🚀 Como Executar (Quick Start)

### Pré-requisitos

- Python 3.12+
- Docker e Docker Compose
- Um _Personal Access Token_ do GitHub
- Crie um .env com :


  ```bash
    GITHUB_TOKEN=seu_token_aqui
    DATABASE_URL=postgresql://postgres:postgres@localhost:5432/github_db-docker-compose up -d (para subir toda a infra do banco de dados)
   ```
-python3 -m venv venv
-source venv/bin/activate 
-pip install -r requirements.txt

### Execução:

- python3 -m src.main
- streamlit run src/dashboard_main.py (para abrir o Dashboard)

#### Principais Métricas Analisadas

Além dos dados brutos (Estrelas, Forks, Issues), este projeto calcula:

**Taxa de Engajamento**: (Watchers / Stars) \* 100. Identifica projetos onde a comunidade acompanha ativamente as atualizações (ex: frameworks core), em oposição a projetos que recebem estrelas apenas como "favoritos".

**Taxa de Contribuição**: (Forks / Stars) \* 100. Mostra a proporção de desenvolvedores que clonam o repositório com intenção de modificar o código ou usá-lo como base arquitetural.

##### Passo a Passo

1. **Clone o repositório e acesse a pasta:**
   ```bash
   git clone [https://github.com/Jpcarvalhoxx/github_trend_analyzer.git](https://github.com/Jpcarvalhoxx/github_trend_analyzer.git)
   cd github_trend_analyzer/data-pipeline
   ```

###### Trabalhos Futuros

A arquitetura atual serve como uma base sólida para a evolução do ecossistema. O principal próximo passo planejado é:

**API RESTful (Java / Spring Boot)**: Desenvolvimento de uma camada de microsserviço utilizando Java e Spring Boot para consumir e expor os dados tratados que hoje residem no PostgreSQL.
