from mongoengine import Document, StringField, IntField, ListField, BooleanField, EnumField
from ..data.category import Category
from ..data.difficulty_level import DifficultyLevel
from ..data.question_type import QuestionType


class QuestionEntity(Document):
    object_id = StringField(primary_key=True)  # You can specify primary_key=True to make it behave as an ID
    category = EnumField(Category)
    question = StringField()
    correct = IntField()
    answers = ListField(StringField())
    type = EnumField(QuestionType)
    difficulty = EnumField(DifficultyLevel)
    is_approved = BooleanField()

    def to_dict(self):
        return {
            'object_id': self.object_id,
            'category': self.category.value if self.category else None,
            'question': self.question,
            'correct': self.correct,
            'answers': self.answers,
            'type': self.type.value if self.type else None,
            'difficulty': self.difficulty.value if self.difficulty else None,
            'is_approved': self.is_approved
            }
