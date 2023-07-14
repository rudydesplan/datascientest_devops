from typing import Optional, List
from pydantic import BaseModel

class Question(BaseModel):
    question: str
    subject: str
    correct: List[str]
    use: str
    answerA: str
    answerB: str
    answerC: str
    answerD: Optional[str] = None
    remark: Optional[str] = None

class TestType(BaseModel):
    use: str

class TestSubjects(BaseModel):
    subjects: List[str]

class NumberOfQuestions(BaseModel):
    number: int

class AuthenticationUser(BaseModel):
    username: str
    password: str
