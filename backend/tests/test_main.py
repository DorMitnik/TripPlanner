import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_auth_register():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/auth/register", json={
            "username": "testuser",
            "password": "testpass"
        })
    assert response.status_code in [200, 400]  # 400 if user already exists

@pytest.mark.asyncio
async def test_auth_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/auth/login", data={
            "username": "testuser",
            "password": "testpass"
        })
    assert response.status_code == 200
