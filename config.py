import os
from dotenv import load_dotenv



class credenciales:
    load_dotenv()  # Carga las variables de entorno desde el archivo .env
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    UCN_SCRAPER_URL = os.getenv("UCN_SCRAPER_URL")
    USUARIO_UCN = os.getenv("USUARIO_UCN")
    CONTRASENA_UCN = os.getenv("CONTRASENA_UCN")
    API_KEY_GEMMINI_IA = os.getenv("API_KEY_GEMMINI_IA")
    API_KEY_GROP_IA = os.getenv("API_KEY_GROP_IA")
    
