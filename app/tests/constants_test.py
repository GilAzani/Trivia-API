class TestConstants:
    TEST_QUESTION = {
        "answers": [
            "no",
            "yes"
            ],
        "category": "Sports",
        "correct": 1,
        "difficulty": "Easy",
        "question": "Does Beitar is the best team??",
        "type": "Yes/No"
    }

    TEST_CORRECT_INDEX_NOT_IN_RANGE_QUESTION = {
        "answers": [
            "no",
            "yes"
            ],
        "category": "Sports",
        "correct": 4,
        "difficulty": "Easy",
        "question": "Does Beitar is the best team??",
        "type": "Yes/No"
    }

    TEST_TOO_MANY_ANSWERS_QUESTION = {
        "answers": [
            "no",
            "yes",
            "wrong"
            ],
        "category": "Sports",
        "correct": 1,
        "difficulty": "Easy",
        "question": "Does Beitar is the best team??",
        "type": "Yes/No"
    }

    TEST_CORRECT_INDEX_NOT_IN_RANGE_NULTI_QUESTION = {
        "answers": [
            "no",
            "yes",
            "maybe",
            "not"
            ],
        "category": "Sports",
        "correct": 5,
        "difficulty": "Easy",
        "question": "Does Beitar is the best team??",
        "type": "Multiple Choice"
    }

    TEST_TOO_MANY_ANSWERS_NULTI_QUESTION = {
        "answers": [
            "no",
            "yes",
            "maybe",
            "not",
            "Hell NO"
            ],
        "category": "Sports",
        "correct": 1,
        "difficulty": "Easy",
        "question": "Does Beitar is the best team??",
        "type": "Multiple Choice"
    }
