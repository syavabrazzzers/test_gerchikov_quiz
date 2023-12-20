import enum
from typing import Type

from pydantic import BaseModel


class MotivationTypes(enum.Enum):
    IN = 'in'
    PR = 'pr'
    PA = 'pa'
    HO = 'ho'
    LU = 'lu'
    NULL = ''


class QuestionSchema(BaseModel):
    text: str
    choices_count: int
    questions: dict[str | int, MotivationTypes | list[MotivationTypes]]
