from flask import Blueprint, request, jsonify
from src.services.questions_service import QuestionsService
from src.data.category import Category
from src.data.difficulty_level import DifficultyLevel
from src.data.question_type import QuestionType


class QuestionsRoute:
    def __init__(self):
        self.blueprint = Blueprint('questions', __name__)
        self.questions_service = QuestionsService()

        # Register routes
        self.register_routes()

    def register_routes(self):
        self.blueprint.route('/questions', methods=['GET'])(self.get_questions)

    def get_questions(self):
        # Get the category query parameter if provided, otherwise set it to None
        category = Category.from_string(request.args.get('category', ""))
        # Get the amount query parameter (required)
        amount = int(request.args.get('amount'))

        difficulty = DifficultyLevel.from_string(request.args.get('difficulty', ""))

        question_type = QuestionType.from_string(request.args.get('type', ""))

        return jsonify(self.questions_service.get_questions(category=category, difficulty=difficulty,
                                                            question_type=question_type, amount=amount))

    def as_blueprint(self):
        return self.blueprint
