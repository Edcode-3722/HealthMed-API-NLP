from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_core import responder_pregunta

app = FastAPI()

class PreguntaRequest(BaseModel):
    pregunta: str

@app.post("/preguntar")
def preguntar(data: PreguntaRequest):
    try:
        respuesta = responder_pregunta(data.pregunta)
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
