from fastapi import APIRouter, Depends, HTTPException
from database import write_data_to_csv
from models import QuestionCreate
from auth import get_current_user
from config import config

router = APIRouter()

@router.post("/")
async def create_question(question: QuestionCreate, current_user: str = Depends(get_current_user)):
    if current_user[0] != config.ADMIN_USERNAME or current_user[1] != config.ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="Operation not allowed")
    write_data_to_csv(question.dict())
    return {"message": "Question added successfully"}
