from typing import Optional, Union, List
from pydantic import BaseModel

class Question(BaseModel):
    question: str
    subject: str
    correct: Union[str, List[str]]
    use: str
    responseA: str
    responseB: str
    responseC: Optional[str] = ""
    responseD: Optional[str] = ""
    remark: Optional[str] = ""

class QuestionCreate(BaseModel):
    question: str
    subject: str
    correct: str
    use: str
    responseA: str
    responseB: str
    responseC: Optional[str] = ""
    responseD: Optional[str] = ""
    remark: Optional[str] = ""

class TestType(BaseModel):
    use: str

class TestSubjects(BaseModel):
    subjects: str

class NumberOfQuestions(BaseModel):
    number: int

class AuthenticationUser(BaseModel):
    username: str
    password: str
