from ..data.category import Category
from ..data.difficulty_level import DifficultyLevel
from ..data.question_type import QuestionType
from ..dal.question_crud import QuestionCRUD
from ..data.question_boundary import QuestionBoundary
from ..validator import Validator
import warnings


class QuestionsService:
    def __init__(self) -> None:
        pass

    def get_questions(self, category: str, difficulty: str, question_type: str, amount: int):
        Validator.validate_get_question(category=category, difficulty=difficulty, question_type=question_type, amount=amount)

        return QuestionCRUD.get_questions_by_type_difficulty_category_and_amount(
            question_type=QuestionType.from_string(question_type),
            question_category=Category.from_string(category),
            question_difficulty=DifficultyLevel.from_string(difficulty),
            amount=amount)

    def post_question(self, question_boundary: dict):
        Validator.validate_question_boundary(question_boundary_dict=question_boundary)
        return QuestionCRUD.create_question_using_entity(question_entity=QuestionBoundary(question_boundary).to_entity())

    def get_question_by_id(self, question_id: str):
        return QuestionCRUD.get_question_by_id(object_id=question_id)

    def delete_question_by_id(self, question_id: str):
        return QuestionCRUD.delete_question(object_id=question_id)

    def approve_question_by_id(self, question_id: str):
        warnings.warn("This method is deprecated. Use direct approval on the DB instead.", DeprecationWarning)
        return QuestionCRUD.update_question(object_id=question_id, **{'is_approved': True})
