# Backend - Automatizacion (FastAPI)

## Resumen
Backend en Python con FastAPI que expone un WebSocket para conversación con IA. Valida tokens de Firebase, gestiona estado de conversación y transmite respuestas por streaming, finalizando con el token `[DONE]`.

## Arquitectura
- `servidorFastapi.py`: servidor principal FastAPI + WebSocket.
- `src/Tex_IA.py`: lógica de IA (Gemma) y estado de conversación.
- `src/Aunth.py`: validación de tokens de Firebase.
- `config.py`: carga de credenciales desde `.env`.
- `src/MytelegramBot.py` y `src/navegador.py`: funciones futuras en desarrollo (pruebas iniciales).

## WebSocket
Ruta:
- `ws://<host>:8080/ws`

Mensajes entrantes (JSON):
- Auth inicial:
  ```json
  {"peticion":"auth","token":"<firebase_token>"}
  ```
- Conversación:
  ```json
  {"peticion":"hablar con ia","mensaje":"..."}
  ```

Mensajes salientes:
- Texto en chunks.
- Fin de stream: `[DONE]`.

Archivo clave:
- `servidorFastapi.py`

## Autenticación
- `src/Aunth.py` usa Firebase Admin SDK para validar el ID token.
- Si el token no es válido, se cierra la conexión.

Archivo clave:
- `src/Aunth.py`

## IA
- `src/Tex_IA.py` usa Google GenAI para streaming.
- Guarda contexto en memoria con `ConversationState`.

Archivo clave:
- `src/Tex_IA.py`

## Configuración
- Variables se cargan desde `.env` en `config.py`.

Ejemplos:
- `TELEGRAM_TOKEN`
- `API_KEY_GEMMINI_IA`

## Ejecutar
```bash
python servidorFastapi.py
```

## Notas
- `src/MytelegramBot.py` y `src/navegador.py` están como pruebas iniciales.
