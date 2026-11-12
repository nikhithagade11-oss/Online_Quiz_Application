import pytest
from app import app
from database import get_questions_by_ids


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
    # First visit the quiz page
    client.get("/quiz")

    # Get the selected question IDs from the session
    with client.session_transaction() as session:
        question_ids = session["question_ids"]

    # Retrieve the correct answers for those questions
    questions = get_questions_by_ids(question_ids)

    # Submit all correct answers
    answers = {
        str(i): question["answer"]
        for i, question in enumerate(questions)
    }

    response = client.post("/result", data=answers)

    assert response.status_code == 200
    assert b"5 / 5" in response.data
    assert b"All answers are correct!" in response.data