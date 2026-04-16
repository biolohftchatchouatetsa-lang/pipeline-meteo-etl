import pandas as pd

def clean_data(df):
    """Nettoie et transforme les données météo"""
    if df.empty:
        print("⚠️ Pas de données à transformer")
        return df
        
    # Duplications
    df = df.drop_duplicates(subset=['ville', 'date'])
    
    # Conversion °F
    df['temp_f'] = df['temp'] * 9/5 + 32
    
    # Catégorie temps (transformation métier)
    def get_categorie(desc):
        if 'clear' in desc.lower():
            return 'Ensoleillé'
        elif 'cloud' in desc.lower():
            return 'Nuageux'
        elif 'rain' in desc.lower():
            return 'Pluvieux'
        else:
            return 'Variable'
    
    df['categorie'] = df['description'].apply(get_categorie)
    
    # Réorganisation colonnes
    return df[['ville', 'temp', 'temp_f', 'categorie', 'date']]

if __name__ == '__main__':
    from fetch_data import fetch_meteo
    df_raw = fetch_meteo()
    df_clean = clean_data(df_raw)
    print("📊 Données transformées :")
    print(df_clean)
    print(f"📈 +{len(df_clean.columns) - len(df_raw.columns)} nouvelles colonnes créées !")