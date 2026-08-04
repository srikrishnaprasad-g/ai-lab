class BaseApplicationException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class ValidationException(BaseApplicationException):
    pass

class RuntimeException(BaseApplicationException):
    pass
