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
    # yield connection
    # Teardown (run after tests)
    connection.disconnect_from_db()

# @pytest.fixture
# def client():
#     with app.test_client() as client:
#         yield client


def test_sanity(client):
    test_question = TestConstants.TEST_QUESTION
    response = client.post("/questions", json=test_question)
    assert response.status_code == 201
