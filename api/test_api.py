import pytest
import aiohttp

@pytest.mark.asyncio
async def test_root():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8000/") as response:
            assert response.status == 200
            data = await response.json()
            assert data == {"mensaje": "API Trivia con PostgreSQL 🎉"}

@pytest.mark.asyncio
async def test_obtener_preguntas():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8000/preguntas") as response:
            assert response.status == 200
            data = await response.json()
            assert isinstance(data, list)
            assert len(data) > 0

@pytest.mark.asyncio
async def test_responder_correcto():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8000/responder", json={"pregunta_id": 1, "respuesta": "D"}) as response:
            assert response.status == 200
            data = await response.json()
            assert data["is_correct"] is True

@pytest.mark.asyncio
async def test_responder_incorrecto():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8000/responder", json={"pregunta_id": 2, "respuesta": "A"}) as response:
            assert response.status == 200
            data = await response.json()
            assert data["is_correct"] is False

@pytest.mark.asyncio
async def test_responder_no_encontrada():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8000/responder", json={"pregunta_id": 999, "respuesta": "A"}) as response:
            assert response.status == 404
            data = await response.json()
            assert data["detail"] == "Pregunta no encontrada"
