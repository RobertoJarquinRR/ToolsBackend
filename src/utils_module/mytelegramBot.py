"""Funciones futuras en desarrollo (pruebas iniciales)."""

import asyncio
from telegram import Bot
from config import credenciales


"""# Quitamos el asyncio.run de aquí adentro
async def enviarmensaje(mensaje):
    token = credenciales.TELEGRAM_TOKEN
    chat_id = credenciales.TELEGRAM_CHAT_ID

    bot = Bot(token=token)
    
    await bot.send_message(chat_id=chat_id, text=mensaje)
    """