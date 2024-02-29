class QuestionSettingNotExistsException(Exception):
    def __init__(self, settings: dict):
        super().__init__(f"couldn't find questions with this settings:{settings}")
