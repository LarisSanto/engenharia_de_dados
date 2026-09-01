# Importando as bibliotecas necessárias
import requests
import pandas as pd

# 1. Definindo a URL da API da Open-Meteo
url_api = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current=temperature_2m,wind_speed_10m"

print("Conectando com a API da Open-Meteo...")

# 2. Fazendo a requisição HTTP
resposta = requests.get(url_api)

if resposta.status_code == 200:
    print("Conexão bem-sucedida! Organizando os dados...")
    
    dados_json = resposta.json()
    dados_clima = [dados_json['current']]
    
    # 3. Transformando em DataFrame do Pandas
    df = pd.DataFrame(dados_clima)
    df['latitude'] = dados_json['latitude']
    df['longitude'] = dados_json['longitude']
    
    print("\n--- Tabela Gerada ---")
    print(df)
    
    # --- ETAPA DE PERSISTÊNCIA LOCAL ---
    print("\nSalvando os arquivos locais...")
    
    # A) Salvando em formato CSV (separado por vírgulas)
    # index=False evita salvar a coluna numérica de índice lateral que o pandas cria
    df.to_csv("dados_clima.csv", index=False)
    print("Arquivo 'dados_clima.csv' salvo com sucesso!")
    
    # B) Salvando em formato XLSX (Excel)
    df.to_excel("dados_clima.xlsx", index=False)
    print("Arquivo 'dados_clima.xlsx' salvo com sucesso!")
    
    # C) Salvando em formato Parquet (formato otimizado de colunas)
    df.to_parquet("dados_clima.parquet", index=False)
    print("Arquivo 'dados_clima.parquet' salvo com sucesso!")

else:
    print(f"Erro ao conectar com a API. Código do erro: {resposta.status_code}")
    