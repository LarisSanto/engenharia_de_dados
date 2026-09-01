# Importando as bibliotecas necessárias
import requests
import pandas as pd
import sys

print("Iniciando o script de simulação Cloud S3...")

# 1. Definindo a URL da API da Open-Meteo
url_api = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current=temperature_2m,wind_speed_10m"
print("Buscando dados da API...")

# Fazendo a requisição HTTP com timeout para evitar travamentos infinitos
try:
    resposta = requests.get(url_api, timeout=10)
except Exception as e:
    print(f"Erro de conexão com a API: {e}")
    sys.exit()

if resposta.status_code == 200:
    print("Conexão bem-sucedida! Processando JSON...")
    dados_json = resposta.json()
    dados_clima = [dados_json['current']]
    
    # Transformando em DataFrame
    df = pd.DataFrame(dados_clima)
    df['latitude'] = dados_json['latitude']
    df['longitude'] = dados_json['longitude']
    
    print("DataFrame estruturado com sucesso.")
    
    # 2. Simulando o armazenamento em formato Cloud Data Lake (Camada Bronze)
    caminho_simulado_s3 = "clima_camada_bronze.parquet"
    print(f"Salvando o arquivo localmente no padrão S3: {caminho_simulado_s3}...")
    
    df.to_parquet(caminho_simulado_s3, index=False)
    
    print("Sucesso! Arquivo Parquet gerado e pronto para o pipeline cloud.")
else:
    print(f"Erro ao conectar com a API. Código do erro: {resposta.status_code}")