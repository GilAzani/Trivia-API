import pytest
from app.__init__ import app  # Import the Flask app
from app.src.db.question_db_connection import QuestionDBConnection
from app.tests.constants_test import TestConstants


# @staticmethod
@pytest.fixture
def client():
    # Setup (run before tests)
    connection = QuestionDBConnection()
    connection.connect_to_test_db()
    with app.test_client() as client:
        yield client

    connection.disconnect_from_db()


def test_sanity(client):
    # suggest question
    test_question = TestConstants.TEST_QUESTION
    response = client.post("/questions", json=test_question)
    assert response.status_code == 201
    question_id = response.get_json().get("object_id")

    # trying to get not approved question
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 404  # until question is approved, it is invisible

    # approving the question
    response = client.put(f"questions/{question_id}/approve")
    assert response.status_code == 200

    # trying to get approved question
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200

    response_json = response.get_json()
    assert response_json.get("answers") == test_question.get("answers")
    assert response_json.get("category") == test_question.get("category")
    assert response_json.get("correct") == test_question.get("correct")
    assert response_json.get("difficulty") == test_question.get("difficulty")
    assert response_json.get("question") == test_question.get("question")
    assert response_json.get("type") == test_question.get("type")

    # deleting the question
    response = client.delete(f"/questions/{question_id}")
    assert response.status_code == 200  # until question is approved, it is invisible

    # trying to get deleted question
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 404


def test_wrong_struct_question_suggestion(client):
    response = client.post("/questions", json=TestConstants.TEST_CORRECT_INDEX_NOT_IN_RANGE_NULTI_QUESTION)
    assert response.status_code == 400

    response = client.post("/questions", json=TestConstants.TEST_CORRECT_INDEX_NOT_IN_RANGE_QUESTION)
    assert response.status_code == 400

    response = client.post("/questions", json=TestConstants.TEST_TOO_MANY_ANSWERS_NULTI_QUESTION)
    assert response.status_code == 400

    response = client.post("/questions", json=TestConstants.TEST_TOO_MANY_ANSWERS_QUESTION)
    assert response.status_code == 400


# at the start of each test, the db is empty, so every question_id shouldn't be exist
def test_get_not_exists_question(client):
    response = client.get("/questions/123")
    assert response.status_code == 404


def test_get_not_valid_amount(client):
    response = client.get("/questions?amount=a")
    assert response.status_code == 400

    response = client.get("/questions?amount=-1")
    assert response.status_code == 400
