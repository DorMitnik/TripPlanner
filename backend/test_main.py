import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_auth_register():
    response = client.post("/auth/signup", json={
        "username": "testuser",
        "password": "testpass",
        "email": "test@gmail.com"
    })
    assert response.status_code in [200, 400]  # 400 if user already exists

def test_auth_login():
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200