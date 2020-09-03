from enum import Enum


class BaseEnum(Enum):

    @property
    def name_value(self):
        return self.name.lower()


class Gender(BaseEnum):
    MALE = 1
    FEMALE = 2

    @property
    def short_code(self):
        return self.name[0]
