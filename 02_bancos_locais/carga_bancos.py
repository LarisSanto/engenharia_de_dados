# Importando as bibliotecas 
import requests
import pandas as pd
from sqlalchemy import create_engine

# 1. Buscando os dados da API da Open-Meteo (mesmo processo de antes)
url_api = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current=temperature_2m,wind_speed_10m"
print("Buscando dados da API...")
resposta = requests.get(url_api)

if resposta.status_code == 200:
    dados_json = resposta.json()
    dados_clima = [dados_json['current']]
    
    # Criando o DataFrame do Pandas
    df = pd.DataFrame(dados_clima)
    df['latitude'] = dados_json['latitude']
    df['longitude'] = dados_json['longitude']
    
    print("Dados extraídos e transformados com sucesso!")
    
    # --- 2. ENVIANDO PARA O BANCO SQL RELACIONAL (SQLite) ---
    # Criando a 'ponte' de conexão (motor) para um banco relacional local baseado em arquivo
    engine_postgres = create_engine('sqlite:///banco_local.db')
    
    # Enviando o DataFrame para virar uma tabela chamada 'tabela_clima' no banco relacional
    df.to_sql('tabela_clima', engine_postgres, if_exists='replace', index=False)
    print("Sucesso! Dados gravados na tabela do banco relacional.")
    
    # --- 3. ENVIANDO PARA O MYSQL (Opcional, caso queira manter) ---
    try:
        engine_mysql = create_engine('mysql+pymysql://root@localhost/mysql')
        df.to_sql('tabela_clima', engine_mysql, if_exists='replace', index=False)
        print("Sucesso! Dados gravados na tabela do MySQL.")
    except Exception as e:
        print("MySQL local ignorado (passou direto pelo erro de serviço).")

else:
    print(f"Erro ao conectar com a API: {resposta.status_code}")
    