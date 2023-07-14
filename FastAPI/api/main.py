from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List
from . import auth, admin, database, questions, config
from .models import QuestionBase, Question

app = FastAPI()

security = HTTPBasic()

# Add a route for verifying the API
@app.get("/ping")
def ping():
    return {"message": "pong"}

# Add a route for fetching questions
@app.get("/questions", response_model=List[Question])
def get_questions(use: str, subject: List[str], count: int, credentials: HTTPBasicCredentials = Depends(security)):
    if not auth.verify_credentials(credentials):
        raise HTTPException(status_code=401, detail="Invalid user credentials")
    if use not in config.VALID_USES:
        raise HTTPException(status_code=400, detail="Invalid use type")
    if not all(s in config.VALID_SUBJECTS for s in subject):
        raise HTTPException(status_code=400, detail="Invalid subject")
    if count not in config.VALID_COUNTS:
        raise HTTPException(status_code=400, detail="Invalid count")
    try:
        return questions.get_questions(use, subject, count)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/admin/questions", response_model=Question)
def create_question(question: QuestionBase, credentials: HTTPBasicCredentials = Depends(security)):
    if not auth.verify_credentials(credentials, admin=True):
        raise HTTPException(status_code=401, detail="Invalid admin credentials")
    try:
        return admin.create_question(question)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error occurred while adding question")
        
# this is still a basic setup and might need further adjustments based on the actual implementation of the auth, admin, database, and questions modules and your specific requirements.
