from bson import ObjectId


# Класс, для проверки корректности входящего идентификатора
class PyObjectId(ObjectId):

    # Метод класса, для получения корректных данных
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    # Метод класса, выполняет проверку идентификатора
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)