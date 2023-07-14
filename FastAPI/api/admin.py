from fastapi import APIRouter, Depends, HTTPException
from database import write_data_to_csv
from models import QuestionIn
from auth import get_current_username, ADMIN_USER

router = APIRouter()

@router.post("/")
async def create_question(question: QuestionIn, current_user: str = Depends(get_current_username)):
    if current_user != ADMIN_USER:
        raise HTTPException(status_code=403, detail="Operation not allowed")
    write_data_to_csv(question.dict())
    return {"message": "Question added successfully"}
