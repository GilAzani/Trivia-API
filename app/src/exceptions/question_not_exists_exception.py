class QuestionNotExistsException(Exception):
    """Exception raised when a question does not exist."""

    def __init__(self, question_id):
        super().__init__(f"Question with ID '{question_id}' does not exist.")

    def __init__(self, message: str):  # noqa811
        super().__init__(message)
