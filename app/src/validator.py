from src.data.question_boundary import QuestionBoundary
from src.data.category import Category
from src.data.difficulty_level import DifficultyLevel
from src.data.question_type import QuestionType
from src.exceptions.data_not_valid_exception import DataNotValidException


class Validator:

    @staticmethod
    def validate_question_boundary(question_boundary_dict: dict):
        object_id, category, question, correct, answers, question_type, difficulty = QuestionBoundary.extract_question_values(question_boundary_dict)

        Validator.validate_object_id(object_id)
        Validator.validate_category(category)
        Validator.validate_question(question)
        Validator.validate_correct(correct)
        Validator.validate_answers(answers)
        Validator.validate_type(question_type)
        Validator.validate_difficulty(difficulty)
        Validator.validate_question_structure(question_type, correct, answers)

    @staticmethod
    def validate_object_id(object_id: str):
        if object_id and not isinstance(object_id, str):
            raise DataNotValidException("question_id")

    @staticmethod
    def validate_category(category: str):
        if category and not isinstance(category, str):
            raise DataNotValidException("question_id")


