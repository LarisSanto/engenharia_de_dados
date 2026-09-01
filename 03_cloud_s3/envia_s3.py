# Importando as bibliotecas
import requests
import pandas as pd

# 1. Buscando os dados da API (mesmo fluxo de sempre)
url_api = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current=temperature_2m,wind_speed_10m"
print("Buscando dados da API...")
resposta = requests.get(url_api)

if resposta.status_code == 200:
    dados_json = resposta.json()
    dados_clima = [dados_json['current']]
    
    df = pd.DataFrame(dados_clima)
    df['latitude'] = dados_json['latitude']
    df['longitude'] = dados_json['longitude']
    
    print("Dados prontos!")
    
    # --- 2. ENVIANDO PARA O AWS S3 ---
    # No ambiente corporativo, salvaríamos direto no bucket assim:
    # nome_do_bucket = "s3://meu-bucket-de-dados-engenharia/clima.parquet"
    # df.to_parquet(nome_do_bucket, index=False)
    
    # Como estamos simulando a estrutura sem uma conta AWS ativa neste exato segundo,
    # vamos salvar o arquivo em formato Parquet com o padrão que as empresas usam no S3 (Data Lake)
    caminho_simulado_s3 = "clima_camada_bronze.parquet"
    
    df.to_parquet(caminho_simulado_s3, index=False)
    print(f"Sucesso! Arquivo gerado no padrão S3: '{caminho_simulado_s3}'")
    print("Na nuvem real, esse comando mandaria o arquivo direto para o balde da Amazon!")

else:
    print(f"Erro ao conectar com a API: {resposta.status_code}")