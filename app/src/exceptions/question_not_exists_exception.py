class QuestionNotExistsException(Exception):
    """Exception raised when a question does not exist."""

    def __init__(self, question_id: str):
        super().__init__(f"Question with ID '{question_id}' does not exist.")
