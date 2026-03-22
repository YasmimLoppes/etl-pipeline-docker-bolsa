import os
import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from dotenv import load_dotenv

# 1. Carrega as variáveis do arquivo .env
load_dotenv()

def extract_data():
    """Extrai cotação do Dólar via API"""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    try:
        response = requests.get(url)
        data = response.json()['USDBRL']
        print(f"✅ Extração: USD/BRL a {data['bid']}")
        return data
    except Exception as e:
        print(f"❌ Erro na extração: {e}")
        return None

def transform_data(data):
    """Tratamento com Pandas"""
    if not data: return None
    df = pd.DataFrame([data])
    df = df[['code', 'codein', 'bid', 'create_date']]
    df.columns = ['moeda_origem', 'moeda_destino', 'valor_cotacao', 'data_api']
    df['valor_cotacao'] = pd.to_numeric(df['valor_cotacao'])
    df['data_extracao'] = datetime.now()
    return df

def load_to_db(df):
    """Carga Segura no PostgreSQL"""
    if df is None: return
    
    # Puxando as credenciais das variáveis de ambiente
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    try:
        engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')
        df.to_sql('cotacoes_dolar', engine, if_exists='append', index=False)
        print("🚀 Carga realizada com sucesso!")
    except Exception as e:
        print(f"❌ Erro na carga: {e}")

if __name__ == "__main__":
    print(f"--- Pipeline Iniciado ({datetime.now()}) ---")
    raw = extract_data()
    clean = transform_data(raw)
    load_to_db(clean)