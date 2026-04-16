from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# Connexion PostgreSQL (vos .env paramètres)
conn_str = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(conn_str)

def load_to_db(df, table='meteo'):
    """Charge les données dans PostgreSQL"""
    try:
        df.to_sql(table, engine, if_exists='append', index=False)
        print(f"✅ {len(df)} lignes chargées dans '{table}'")
        
        # Vérification
        result = pd.read_sql(f"SELECT * FROM {table} ORDER BY temp DESC", engine)
        print("🔍 Vérification SQL :")
        print(result)
        
    except Exception as e:
        print(f"❌ Erreur DB: {e}")

if __name__ == '__main__':
    from transform import clean_data
    from fetch_data import fetch_meteo
    df_clean = clean_data(fetch_meteo())
    load_to_db(df_clean)

    # Bonus : Requêtes avancées
print("\n📊 ANALYSE SQL :")
print(pd.read_sql("SELECT ville, ROUND(AVG(temp)::numeric, 2) as temp_moy FROM meteo GROUP BY ville ORDER BY temp_moy DESC", engine))