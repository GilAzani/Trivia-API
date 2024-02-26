from uuid import uuid4
from src.data.question_entity import QuestionEntity
from src.data.category import Category
from src.data.difficulty_level import DifficultyLevel
from src.data.question_type import QuestionType


class QuestionCRUD:
    @staticmethod
    def create_question(question_entity: str, correct: int, answers: list[str], question_type: QuestionType,
                        category: Category, difficulty: DifficultyLevel):
        object_id = str(uuid4())  # Generate a UUID for object_id
        question_entity = QuestionEntity(
            object_id=object_id,
            category=category,
            question=question_entity,
            correct=correct,
            answers=answers,
            type=question_type,
            difficulty=difficulty,
            is_approved=False  # default value is flase, admin needs to approve the question
        )
        question_entity.save()
        return question_entity.to_dict()

    # @staticmethod
    # def create_question(question_entity: str, correct: int, answers: list[str], question_type: QuestionType,
    #                     category: Category, difficulty: DifficultyLevel, is_approved: bool):
    #     object_id = str(uuid4())  # Generate a UUID for object_id
    #     question_entity = QuestionEntity(
    #         object_id=object_id,
    #         category=category,
    #         question=question_entity,
    #         correct=correct,
    #         answers=answers,
    #         type=question_type,
    #         difficulty=difficulty,
    #         is_approved=is_approved
    #     )
    #     question_entity.save()
    #     return question_entity.to_dict()

    @staticmethod
    def get_question_by_id(object_id):
        return QuestionEntity.objects(object_id=object_id).first()

    @staticmethod
    def update_question(object_id, **kwargs):
        question = QuestionEntity.objects(object_id=object_id).first()
        if question:
            for key, value in kwargs.items():
                setattr(question, key, value)
            question.save()
        return question

    @staticmethod
    def delete_question(object_id):
        question = QuestionEntity.objects(object_id=object_id).first()
        if question:
            question.delete()
            return True
        return False

    @staticmethod
    def get_questions_by_type_difficulty_category_and_amount(question_type: QuestionType, question_category: Category,
                                                             question_difficulty: DifficultyLevel, amount: int):
        pipeline = [
            {"$match": {"type": question_type.value,
                        "difficulty": question_difficulty.value,
                        "category": question_category.value,
                        "is_approved": True}},
            {"$sample": {"size": amount}}
        ]

        # Execute the aggregation pipeline
        cursor = QuestionEntity.objects.aggregate(*pipeline)

        # Convert the cursor to a list of dictionaries
        random_questions = list(cursor)

        return random_questions
