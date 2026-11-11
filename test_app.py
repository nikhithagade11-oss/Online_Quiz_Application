
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Online Quiz Application" in response.data


def test_quiz_page(client):
    response = client.get("/quiz")
    assert response.status_code == 200
    assert b"Online Quiz Application" in response.data


def test_quiz_result(client):
    response = client.post("/result", data={
        "0": "All of these",
        "1": "def",
        "2": "Central Processing Unit",
        "3": "bool",
        "4": "Guido van Rossum"
    })

    assert response.status_code == 200
    assert b"5 / 5" in response.data
