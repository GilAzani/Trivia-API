from ..data.question_entity import QuestionEntity
from ..data.category import Category
from ..data.question_type import QuestionType
from ..data.difficulty_level import DifficultyLevel


class QuestionBoundary:

    def __init__(self, data: dict) -> None:
        self.object_id = data.get('object_id')
        self.category = data.get('category')
        self.question = data.get('question')
        self.correct = data.get('correct')
        self.answers = data.get('answers')
        self.type = data.get('type')
        self.difficulty = data.get('difficulty')

    def from_entity(self, question_entity: QuestionEntity) -> None:
        self.object_id = question_entity.object_id  # You can specify primary_key=True to make it behave as an ID
        self.category = question_entity.category
        self.question = question_entity.question
        self.correct = question_entity.correct
        self.answers = question_entity.answers
        self.type = question_entity.type
        self.difficulty = question_entity.difficulty

    def to_entity(self) -> QuestionEntity:
        return QuestionEntity(
            object_id=self.object_id,
            category=Category.from_string(self.category),
            question=self.question,
            correct=self.correct,
            answers=self.answers,
            type=QuestionType.from_string(self.type),
            difficulty=DifficultyLevel.from_string(self.difficulty),
            is_approved=False  # as default a question is not approved
        )

    @staticmethod
    def extract_question_values(question_boundary_dict: dict):
        object_id = question_boundary_dict.get('object_id')
        category = question_boundary_dict.get('category')
        question = question_boundary_dict.get('question')
        correct = question_boundary_dict.get('correct')
        answers = question_boundary_dict.get('answers')
        question_type = question_boundary_dict.get('type')
        difficulty = question_boundary_dict.get('difficulty')
        return object_id, category, question, correct, answers, question_type, difficulty
