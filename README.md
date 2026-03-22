# 🚀 Pipeline ETL de Cotação de Moedas com Docker

Olá! Eu sou a **Yasmin**, Engenheira de Dados, e este é um projeto de pipeline automatizado para extração, transformação e carga (ETL) de dados financeiros.

## 🛠️ Tecnologias Utilizadas
* **Python**: Linguagem principal para o script de automação.
* **Pandas**: Biblioteca para manipulação e limpeza de dados.
* **Docker & Docker Compose**: Orquestração do banco de dados e ferramentas em containers.
* **PostgreSQL**: Banco de dados relacional para armazenamento do histórico.
* **Adminer**: Interface visual para gerenciamento de dados.

## 📋 Como o Projeto Funciona
O pipeline realiza as seguintes etapas:
1. **Extração**: Coleta o valor atual do Dólar (USD/BRL) via API de Economia.
2. **Transformação**: Trata os dados brutos e adiciona um timestamp de consulta usando Pandas.
3. **Carga**: Insere os dados processados em um banco de dados PostgreSQL rodando em um container Docker.

## 🚀 Como Executar
1. Clone este repositório.
2. No terminal, suba os containers:
   ```bash
   docker-compose up -d