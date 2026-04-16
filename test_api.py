import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv('API_KEY')
print(f"🔑 Clé détectée: {api_key[:10]}...{len(api_key)} caractères")

url = f"https://api.openweathermap.org/data/2.5/weather?q=Paris&appid={api_key}&units=metric"
response = requests.get(url)
print(f"📡 Status: {response.status_code}")
print(f"📄 Réponse: {response.json()}")