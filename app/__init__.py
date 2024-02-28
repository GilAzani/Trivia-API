from flask import Flask
from .src.endpoints.question_route import QuestionsRoute
from .src.db.question_db_connection import QuestionDBConnection


app = Flask(__name__)

# questions_service = QuestionsService()
# return questions_service.get_questions(genre=genre, amount=amount, difficulty=difficulty)
question_db_connector = QuestionDBConnection()

questions_route = QuestionsRoute()
app.register_blueprint(questions_route.as_blueprint())


if __name__ == '__main__':
    try:
        question_db_connector.connect_to_db()   # Connect to MongoDB
        app.run()
    finally:
        question_db_connector.disconnect_from_db()  # Disconnect from MongoDB
