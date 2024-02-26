from enum import Enum


class DifficultyLevel(Enum):
    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'

    @classmethod
    def from_string(cls, difficulty_str):
        # Convert input string to lowercase for case-insensitive comparison
        difficulty_str_lower = difficulty_str.lower()

        # Iterate over enum members
        for difficulty in cls:
            # Check if the lowercase value of the enum member matches the lowercase input string
            if difficulty.value.lower() == difficulty_str_lower:
                return difficulty

        # If no match is found, return None
        return cls.EASY  # easy is the default level
