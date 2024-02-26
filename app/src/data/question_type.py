from enum import Enum


class QuestionType(Enum):
    YES_NO = "Yes/No"
    MULTI_CHOICE = "Multiple Choice"

    @classmethod
    def from_string(cls, question_type_str: str):
        # Convert input string to lowercase for case-insensitive comparison
        question_type_str_lower = question_type_str.lower()

        # Iterate over enum members
        for question_type in cls:
            # Check if the lowercase value of the enum member matches the lowercase input string
            if question_type.value.lower() == question_type_str_lower:
                return question_type

        # If no match is found, return None
        return cls.MULTI_CHOICE  # Multiple Choice question is the default type
