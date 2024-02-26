from src.data.category import Category
from src.data.difficulty_level import DifficultyLevel
from src.data.question_type import QuestionType
from src.dal.question_crud import QuestionCRUD


class QuestionsService:
    def __init__(self) -> None:
        pass

    def get_questions(self, category: Category, difficulty: DifficultyLevel, question_type: QuestionType, amount: int = 1):
        return QuestionCRUD.get_questions_by_type_difficulty_category_and_amount(question_type=question_type,
                                                                                 question_category=category,
                                                                                 question_difficulty=difficulty,
                                                                                 amount=amount)
