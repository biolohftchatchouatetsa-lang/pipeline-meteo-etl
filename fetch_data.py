import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_meteo(villes=['Paris', 'Lyon', 'Marseille']):
    api_key = os.getenv('API_KEY')
    data = []
    for ville in villes:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric"
        resp = requests.get(url).json()
        
        # Vérification erreur API
        if 'cod' in resp and resp['cod'] != 200:
            print(f"❌ Erreur API pour {ville}: {resp.get('message', 'Inconnu')}")
            continue
            
        try:
            meteo = {
                'ville': ville,
                'temp': resp['main']['temp'],
                'description': resp['weather'][0]['description'],
                'date': pd.Timestamp.now().date()
            }
            data.append(meteo)
        except KeyError as e:
            print(f"❌ Erreur données {ville}: {e}")
            continue
            
    return pd.DataFrame(data)

if __name__ == '__main__':
    df = fetch_meteo()
    print("✅ Données récupérées :")
    print(df)