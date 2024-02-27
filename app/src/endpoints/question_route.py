from flask import Blueprint, request, jsonify
from src.services.questions_service import QuestionsService
from src.data.category import Category
from src.data.difficulty_level import DifficultyLevel
from src.data.question_type import QuestionType
from src.data.question_boundary import QuestionBoundary
from src.exceptions.question_not_exists_exception import QuestionNotExistsException


class QuestionsRoute:
    def __init__(self):
        self.blueprint = Blueprint('questions', __name__)
        self.questions_service = QuestionsService()

        # Register routes
        self.register_routes()

    def register_routes(self):
        self.blueprint.route('/questions', methods=['GET'])(self.get_questions)
        self.blueprint.route('/questions', methods=['POST'])(self.suggest_question)
        self.blueprint.route('/questions/<question_id>', methods=['GET'])(self.get_question_by_id)

    def get_questions(self):
        # Get the category query parameter if provided, otherwise set it to None
        category = Category.from_string(request.args.get('category', ""))
        # Get the amount query parameter (required)
        amount = int(request.args.get('amount'))

        difficulty = DifficultyLevel.from_string(request.args.get('difficulty', ""))

        question_type = QuestionType.from_string(request.args.get('type', ""))

        return jsonify(self.questions_service.get_questions(category=category, difficulty=difficulty,
                                                            question_type=question_type, amount=amount)), 200

    def suggest_question(self):
        data = request.json  # Get the JSON data from the request body
        question_boundary = QuestionBoundary(data)  # Create a QuestionBoundary instance from the JSON data
        return jsonify(self.questions_service.post_question(question_boundary)), 201

    def get_question_by_id(self, question_id):
        try:
            return jsonify(self.questions_service.get_question_by_id(question_id)), 200
        except QuestionNotExistsException as e:
            return jsonify({'error': str(e)}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def as_blueprint(self):
        return self.blueprint
