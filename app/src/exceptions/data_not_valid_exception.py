class DataNotValidException(Exception):
    """Exception raised when a question does not exist."""

    def __init__(self, parameter_name):
        super().__init__(f"{parameter_name} value not valid")
