from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from database import get_random_questions
from models import Question
from utils import validate_subjects, validate_use_case, validate_number_of_questions
from auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[Optional[Question]], summary="Get Random Questions", 
    description="Fetches a set of random questions based on the provided subjects and use case. You can specify the number of questions.")
async def read_questions(subject: str, use: str, number: int, current_user: str = Depends(get_current_user)):
    validate_subjects(subject)
    validate_use_case(use)
    validate_number_of_questions(number)
    questions = None
    try:
        questions = get_random_questions(subject, use, number)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found.")
    return questions
