# 📈 Pipeline de Coleta de Dados Financeiros em Tempo Real

Este projeto consiste em uma automação desenvolvida em Python para extração, tratamento e consolidação de dados financeiros em tempo real através da **AwesomeAPI**.

## 🛠️ Tecnologias Utilizadas
* **Python 3.11**
* **Requests** (Consumo de API REST)
* **Pandas** (Estruturação e Manipulação de Dados)

## 🔄 Fluxo da Aplicação
1. Conexão HTTP REST com a AwesomeAPI.
2. Extração das cotações atualizadas das moedas: Dólar (USD), Euro (EUR) e Bitcoin (BTC).
3. Tratamento dos dados e inclusão de timestamp de execução.
4. Exportação estruturada para formato CSV (`relatorio_cotacoes.csv`).

## 🚀 Como Executar
1. Clone o repositório ou baixe os arquivos.
2. Instale as dependências executando:
   ```bash
   pip install requests pandas
   ```
   Execute o script principal:
   ```bash
   python app.py
