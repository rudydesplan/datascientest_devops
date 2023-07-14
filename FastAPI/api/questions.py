from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_random_questions
from models import Question
from utils import validate_subjects, validate_use_case
from auth import get_current_username

router = APIRouter()

@router.get("/", response_model=List[Question])
async def read_questions(subjects: List[str], use: str, number: int, current_user: str = Depends(get_current_username)):
    validate_subjects(subjects)
    validate_use_case(use)
    try:
        questions = get_random_questions(subjects, use, number)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return questions