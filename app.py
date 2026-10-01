import requests
import pandas as pd
from datetime import datetime

def buscar_dados():
    # Busca cotações de moedas em tempo real
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        
        # Estrutura os dados recebidos
        lista_dados = []
        for chave, item in dados.items():
            lista_dados.append({
                "Moeda": item["name"],
                "Valor (R$)": float(item["bid"]),
                "Variação (%)": float(item["pctChange"]),
                "Máxima": float(item["high"]),
                "Mínima": float(item["low"]),
                "Data/Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        
        return pd.DataFrame(lista_dados)
    else:
        print("Erro ao acessar a API.")
        return None

def processar_e_salvar():
    df = buscar_dados()
    if df is not None:
        # Salva os dados em formato CSV organizado
        nome_arquivo = "relatorio_cotacoes.csv"
        df.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")
        print("Relatório gerado com sucesso: " + nome_arquivo)
        print("\n--- Visualização dos Dados ---")
        print(df)

if __name__ == "__main__":
    processar_e_salvar()
