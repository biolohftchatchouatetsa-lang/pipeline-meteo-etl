#!/usr/bin/env python3
"""Pipeline ETL Météo Complet"""
from fetch_data import fetch_meteo
from transform import clean_data
from load import load_to_db
import logging

# Logs professionnels
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_pipeline():
    """Exécute le pipeline ETL complet"""
    logger.info("🚀 Démarrage pipeline ETL Météo")
    
    # 1. Extraction
    logger.info("📡 Extraction données API...")
    df_raw = fetch_meteo()
    
    # 2. Transformation  
    logger.info("🔄 Transformation des données...")
    df_clean = clean_data(df_raw)
    
    # 3. Loading
    logger.info("💾 Chargement PostgreSQL...")
    load_to_db(df_clean)
    
    logger.info("✅ Pipeline ETL terminé avec succès !")

if __name__ == '__main__':
    run_pipeline()