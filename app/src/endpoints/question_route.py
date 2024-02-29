from flask import Blueprint, request, jsonify
import warnings
from ..services.questions_service import QuestionsService
from ..exceptions.question_not_exists_exception import QuestionNotExistsException
from ..exceptions.data_not_valid_exception import DataNotValidException
from ..exceptions.question_setting_not_exists_exception import QuestionSettingNotExistsException
from ..constants import Constants


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
        self.blueprint.route('/questions/<question_id>', methods=['DELETE'])(self.delete_question_by_id)
        self.blueprint.route('/questions/<question_id>/approve', methods=['PUT'])(self.approve_question_by_id)

    def get_questions(self):
        try:
            # Get the category query parameter if provided, otherwise set it to None
            category = request.args.get('category', "")
            # Get the amount query parameter (required)
            amount = int(request.args.get('amount', 1))

            difficulty = request.args.get('difficulty', "")

            question_type = request.args.get('type', "")

            return jsonify(self.questions_service.get_questions(category=category, difficulty=difficulty,
                                                                question_type=question_type, amount=amount)), Constants.SUCCESS_CODE  # noqa501
        except ValueError as e:
            return jsonify({'error': str(e)}), Constants.BAD_REQUEST_ERROR_CODE
        except DataNotValidException as e:
            return jsonify({'error': str(e)}), Constants.BAD_REQUEST_ERROR_CODE
        except QuestionSettingNotExistsException as e:
            return jsonify({'error': str(e)}), Constants.NOT_EXISTS_ERROR_CODE
        except Exception as e:
            return jsonify({'error': str(e)}), Constants.INTERNAL_ERROR

    def suggest_question(self):
        try:
            data = request.json  # Get the JSON data from the request body
            return jsonify(self.questions_service.post_question(data)), Constants.CREATED_CODE
        except DataNotValidException as e:
            return jsonify({'error': str(e)}), Constants.BAD_REQUEST_ERROR_CODE
        except Exception as e:
            return jsonify({'error': str(e)}), Constants.INTERNAL_ERROR

    def get_question_by_id(self, question_id):
        try:
            return jsonify(self.questions_service.get_question_by_id(question_id)), Constants.SUCCESS_CODE
        except QuestionNotExistsException as e:
            return jsonify({'error': str(e)}), Constants.NOT_EXISTS_ERROR_CODE
        except Exception as e:
            return jsonify({'error': str(e)}), Constants.INTERNAL_ERROR

    def approve_question_by_id(self, question_id):
        warnings.warn("This method is deprecated. Use direct approval on the DB instead.", DeprecationWarning)
        try:
            return jsonify(self.questions_service.approve_question_by_id(question_id)), Constants.SUCCESS_CODE
        except QuestionNotExistsException as e:
            return jsonify({'error': str(e)}), Constants.NOT_EXISTS_ERROR_CODE
        except Exception as e:
            return jsonify({'error': str(e)}), Constants.INTERNAL_ERROR

    def delete_question_by_id(self, question_id):
        try:
            return jsonify(self.questions_service.delete_question_by_id(question_id)), Constants.SUCCESS_CODE
        except QuestionNotExistsException as e:
            return jsonify({'error': str(e)}), Constants.NOT_EXISTS_ERROR_CODE
        except Exception as e:
            return jsonify({'error': str(e)}), Constants.INTERNAL_ERROR

    def as_blueprint(self):
        return self.blueprint
