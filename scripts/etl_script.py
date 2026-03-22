import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

import pandas as pd
import requests
from sqlalchemy import create_engine
from datetime import datetime

# 1. Configurações de Concessão (Sua identidade de Engenheira de Dados)
USER = "yasmin_data_eng"
PASSWORD = "2519"
HOST = "localhost"
PORT = "5432"
DB_NAME = "banco_cotacao"

# URL de conexão para o SQLAlchemy
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

def rodar_etl():
    try:
        print("1. Extraindo preço do Dólar da API...")
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        response = requests.get(url)
        dados = response.json()['USDBRL']

        print("2. Transformando dados com Pandas...")
        df = pd.DataFrame([dados])
        df['data_consulta'] = datetime.now()
        df = df[['code', 'codein', 'bid', 'data_consulta']]

        print("3. Salvando no Banco de Dados (Docker)...")
        engine = create_engine(DATABASE_URL)
        df.to_sql('historico_dolar', engine, if_exists='append', index=False)

        print("✅ Dados do Dólar salvos no Docker com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro no Pipeline: {e}")

if __name__ == "__main__":
    rodar_etl()