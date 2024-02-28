from .data.question_boundary import QuestionBoundary
from .data.question_type import QuestionType
from .exceptions.data_not_valid_exception import DataNotValidException


class Validator:

    @staticmethod
    def validate_question_boundary(question_boundary_dict: dict):
        object_id, category, question, correct, answers, question_type, difficulty = QuestionBoundary.extract_question_values(question_boundary_dict)  # noqa501

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
            raise DataNotValidException("category")

    @staticmethod
    def validate_question(question: str):
        if not isinstance(question, str):
            raise DataNotValidException("question")

    @staticmethod
    def validate_correct(correct: int):
        if not isinstance(correct, int):
            raise DataNotValidException("correct")

    @staticmethod
    def validate_answers(answers: list[str]):
        if not isinstance(answers, list):
            raise DataNotValidException("answers")

        for index, answer in enumerate(answers):
            if not isinstance(answer, str):
                raise DataNotValidException(f"answers, index = {index}")

    @staticmethod
    def validate_type(type: str):
        if type and not isinstance(type, str):
            raise DataNotValidException("type")

    @staticmethod
    def validate_difficulty(difficulty: str):
        if difficulty and not isinstance(difficulty, str):
            raise DataNotValidException("difficulty")

    @staticmethod
    def validate_question_structure(question_type, correct: int, answers: list[str]):
        question_type_enum = QuestionType.from_string(question_type_str=question_type)
        if not question_type_enum:
            raise DataNotValidException("question_type")  # type must be yes/no or multiple

        validation_rules = {
            QuestionType.YES_NO: Validator.validate_yes_no_type,
            QuestionType.MULTI_CHOICE: Validator.validate_multi_choice_type,
        }

        validation_func = validation_rules[question_type_enum]
        validation_func(correct, answers)

    @staticmethod
    def validate_yes_no_type(correct: int, answers: list[str]):
        answers_len = len(answers)
        if correct + 1 > answers_len or answers_len != 2:
            raise DataNotValidException("question_structure")

    @staticmethod
    def validate_multi_choice_type(correct: int, answers: list[str]):
        answers_len = len(answers)
        if correct + 1 > answers_len or answers_len != 4:
            raise DataNotValidException("question_structure")

    @staticmethod
    def validate_amount_requested(amount: int):
        if amount <= 0 and not isinstance(amount, int):
            raise DataNotValidException("amount")

    @staticmethod
    def validate_get_question(category: str, difficulty: str, question_type: str, amount: int):
        Validator.validate_amount_requested(amount=amount)
        Validator.validate_category(category=category)
        Validator.validate_difficulty(difficulty=difficulty)
        Validator.validate_type(type=question_type)
