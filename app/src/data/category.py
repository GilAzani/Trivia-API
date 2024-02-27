from enum import Enum
from src.validator import Validator


class Category(Enum):
    HISTORY = 'History'
    SCIENCE = 'Science'
    LITERATURE = 'Literature'
    GEOGRAPHY = 'Geography'
    SPORTS = 'Sports'
    MOVIES = 'Movies'
    MUSIC = 'Music'
    GENERAL_KNOWLEDGE = 'General Knowledge'

    @classmethod
    def from_string(cls, category_str):
        Validator.validate_category(category=category_str)
        if not category_str:
            return None
        # Convert input string to lowercase for case-insensitive comparison
        category_str_lower = category_str.lower()

        # Iterate over enum members
        for category in cls:
            # Check if the lowercase value of the enum member matches the lowercase input string
            if category.value.lower() == category_str_lower:
                return category

        # If no match is found, return None as default
        return None
