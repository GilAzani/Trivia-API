from src.data.category import Category
from src.data.difficulty_level import DifficultyLevel
from src.data.question_type import QuestionType
from src.dal.question_crud import QuestionCRUD
from src.data.question_boundary import QuestionBoundary


class QuestionsService:
    def __init__(self) -> None:
        pass

    def get_questions(self, category: Category, difficulty: DifficultyLevel, question_type: QuestionType, amount: int = 1):

        return QuestionCRUD.get_questions_by_type_difficulty_category_and_amount(question_type=question_type,
                                                                                 question_category=category,
                                                                                 question_difficulty=difficulty,
                                                                                 amount=amount)

    def post_question(self, question_boundary: QuestionBoundary):
        return QuestionCRUD.create_question_using_entity(question_entity=question_boundary.to_entity())

    def get_question_by_id(self, question_id: str):
        return QuestionCRUD.get_question_by_id(object_id=question_id)
