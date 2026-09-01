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
    
    # --- 2. ENVIANDO PARA O POSTGRESQL ---
    # Criando a 'ponte' de conexão (motor) para o PostgreSQL local
    # Padrão no Codespace: usuario 'postgres', sem senha, na porta local
    engine_postgres = create_engine('postgresql+psycopg2://postgres@localhost/postgres')
    
    # Enviando o DataFrame para virar uma tabela chamada 'tabela_clima' no PostgreSQL
    # if_exists='replace' significa que se a tabela já existir, ela é recriada
    df.to_sql('tabela_clima', engine_postgres, if_exists='replace', index=False)
    print("Sucesso! Dados gravados na tabela do PostgreSQL.")
    
    # --- 3. ENVIANDO PARA O MYSQL ---
    # Criando a 'ponte' de conexão para o MySQL local
    # Padrão no Codespace: usuario 'root', sem senha
    engine_mysql = create_engine('mysql+pymysql://root@localhost/mysql')
    
    # Enviando o DataFrame para virar uma tabela chamada 'tabela_clima' no MySQL
    df.to_sql('tabela_clima', engine_mysql, if_exists='replace', index=False)
    print("Sucesso! Dados gravados na tabela do MySQL.")

else:
    print(f"Erro ao conectar com a API: {resposta.status_code}")