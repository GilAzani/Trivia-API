from flask import Flask
from src.endpoints.question_route import QuestionsRoute
from src.db.question_db_connection import question_DB_connection

app = Flask(__name__)

# questions_service = QuestionsService()
# return questions_service.get_questions(genre=genre, amount=amount, difficulty=difficulty)

questions_route = QuestionsRoute()

app.register_blueprint(questions_route.as_blueprint())


if __name__ == '__main__':
    question_DB_connection()   # Connect to MongoDB
    app.run()
