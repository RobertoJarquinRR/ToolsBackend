from google import genai
from config import credenciales
from google.genai import types
from typing import Any, AsyncIterator, cast, List, Optional


from dataclasses import dataclass, field

@dataclass
class Turn:
    role: str 
    content: str

@dataclass
class ConversationState:
    turns: List[Turn] = field(default_factory=list)

    def add_user(self, text: str) -> None:
        self.turns.append(Turn("user", text))

    def add_assistant(self, text: str) -> None:
        self.turns.append(Turn("model", text))

    def last_n_contents(self, n: int = 8) -> List[types.Content]:
        out: List[types.Content] = []
        for t in self.turns[-n:]:
            out.append(
                types.Content(
                    role=t.role,
                    parts=[types.Part(text=t.content)]
                )
            )
        return out

client = genai.Client(api_key=credenciales.API_KEY_GEMMINI_IA)


class Ia:
    def __init__(self, state: ConversationState):
        self.state = ConversationState()
        
    async def preguntar_a_gemma(self,texto: str) -> AsyncIterator[types.GenerateContentResponse]:
            self.state.add_user(texto)
            contents = self.state.last_n_contents(8)

            stream = await client.aio.models.generate_content_stream(
                model="gemma-3-27b-it",
                contents=cast(Any, contents),
            )

            async def tee() -> AsyncIterator[types.GenerateContentResponse]:
                partes: List[str] = []
                async for chunk in stream:
                    txt: Optional[str] = getattr(chunk, "text", None)
                    if txt is not None:
                        partes.append(txt)
                    yield chunk  

                self.state.add_assistant("".join(partes).strip())

            return tee()

async def Streamer(texto):
    try:
        response = await client.aio.models.generate_content_stream(
            model= "",
            contents=texto
            
        )
        
        return
    except Exception as e:
        return f"Error: {e}"

