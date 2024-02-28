from uuid import uuid4
from ..data.question_entity import QuestionEntity
from ..data.category import Category
from ..data.difficulty_level import DifficultyLevel
from ..data.question_type import QuestionType
from ..exceptions.question_not_exists_exception import QuestionNotExistsException


class QuestionCRUD:
    @staticmethod
    def create_question(question: str, correct: int, answers: list[str], question_type: QuestionType,
                        category: Category, difficulty: DifficultyLevel):
        object_id = str(uuid4())  # Generate a UUID for object_id
        question_entity = QuestionEntity(
            object_id=object_id,
            category=category,
            question=question,
            correct=correct,
            answers=answers,
            type=question_type,
            difficulty=difficulty,
            is_approved=False  # default value is flase, admin needs to approve the question
        )
        question_entity.save()
        return {"object_id": question_entity.object_id}

    @staticmethod
    def create_question_using_entity(question_entity: QuestionEntity):
        question_entity.object_id = str(uuid4())  # Assign the generated UUID to object_id
        question_entity.save()
        return {"object_id": question_entity.object_id}

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
    def get_question_by_id(object_id: str):
        question = QuestionEntity.objects(object_id=object_id).first()
        if question and question.is_approved is not False:
            return question.to_dict()
        raise QuestionNotExistsException(object_id)

    @staticmethod
    def update_question(object_id, **kwargs):
        question = QuestionEntity.objects(object_id=object_id).first()
        if question:
            for key, value in kwargs.items():
                setattr(question, key, value)
            question.save()
            return
        raise QuestionNotExistsException(object_id)

    @staticmethod
    def delete_question(object_id):
        question = QuestionEntity.objects(object_id=object_id).first()
        if question:
            question.delete()
            return
        raise QuestionNotExistsException(object_id)

    @staticmethod
    def get_questions_by_type_difficulty_category_and_amount(question_type: QuestionType, question_category: Category,
                                                             question_difficulty: DifficultyLevel, amount: int):
        settings = {
                "type": question_type.value if question_type else None,
                "difficulty": question_difficulty.value if question_difficulty else None,
                "category": question_category.value if question_category else None,
                "is_approved": True
            }

        filtered_settings = {key: value for key, value in settings.items() if value is not None}

        pipeline = [
            {"$match": filtered_settings},
            {"$sample": {"size": amount}}
        ]

        # Execute the aggregation pipeline
        cursor = QuestionEntity.objects.aggregate(*pipeline)

        # Convert the cursor to a list of dictionaries
        random_questions = list(cursor)

        return random_questions
