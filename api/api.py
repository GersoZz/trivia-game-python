from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import os

app = FastAPI()

DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class RespuestaUsuario(BaseModel):
    pregunta_id: int
    respuesta: str

@app.get("/")
async def root():
    return {"mensaje": "API Trivia con PostgreSQL 🎉"}

@app.get("/preguntas")
async def obtener_preguntas():
    async with SessionLocal() as session:
        result = await session.execute(text("SELECT * FROM preguntas"))
        rows = result.fetchall()
        preguntas = []
        for row in rows:
            preguntas.append({
                "id": row.id,
                "pregunta": row.pregunta,
                "opciones": {
                    "a": row.opcion_a,
                    "b": row.opcion_b,
                    "c": row.opcion_c,
                    "d": row.opcion_d,
                }
            })
        return preguntas

@app.post("/responder")
async def responder(data: RespuestaUsuario):
    async with SessionLocal() as session:
        result = await session.execute(text("SELECT respuesta_correcta FROM preguntas WHERE id = :id"), {"id": data.pregunta_id})
        row = result.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Pregunta no encontrada")
        if data.respuesta == row.respuesta_correcta:
            return {"is_correct": True}
        else:
            return {"is_correct": False}
