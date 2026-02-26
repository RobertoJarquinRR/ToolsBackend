import asyncio
import sys
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from src.ia_module import tex_IA
from src.auth_module import auth


class conexion:
    def __init__(self, ws:WebSocket):
        self.ws = ws
        self.authenticated = False
    
    
    async def accept(self):
        await self.ws.accept()
        print("aceptado")
    async def sendtext(self, mensaje:str):
        await self.ws.send_text(mensaje)
        
    async def close(self, code :int):
        await self.ws.close()


class wshandler:
    async def run(self, con: conexion):
        iaState = tex_IA.ConversationState()
        ia = tex_IA.Ia(iaState)
        while True:
            data = await con.ws.receive_json()
            peticion = data.get("peticion")

            
            match peticion:
                case "Hola inicial":
                    await con.sendtext("hola")
                case "auth":
                    token = data.get("token")
                    ok = auth.validartoken(token)
                    if not ok:
                        await con.sendtext("usuario no encontrado")
                        
                        await con.close(1000)
                        return
                    
                    con.authenticated = True
                    
                case "hablar con ia":
                    if not con.authenticated:
                        await con.sendtext("no autentificado")
                        continue
                    
                    mensaje = data.get("mensaje")
                    if not mensaje:
                        await con.sendtext("falta mensaje")
                        continue
                    
                    print(mensaje)
                    
                    
                    
                    stream = await ia.preguntar_a_gemma(mensaje)
                    async for chunk in stream:
                        texto = getattr(chunk, "text", None)
                        if texto:
                            await con.sendtext(texto)
                            
                    await con.sendtext("[DONE]")

app = FastAPI()
handler = wshandler()

@app.websocket("/ws")
async def websocket_endpoint(Websocket: WebSocket):
    con = conexion(Websocket)
    await con.accept()
    try:
        await handler.run(con)
    except WebSocketDisconnect:
        print("cliente desconectado")


if __name__ == "__main__":
    if sys.platform == "win32" and hasattr(asyncio, "WindowsProactorEventLoopPolicy"):
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())  # type: ignore[attr-defined]
    uvicorn.run(
        "servidorFastapi:app",
        host="0.0.0.0",  
        port=8000,
        reload=True,
        loop="asyncio",
        
    )


