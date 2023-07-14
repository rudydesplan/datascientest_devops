from fastapi import FastAPI
from questions import router as questions_router
from admin import router as admin_router

app = FastAPI()

app.include_router(questions_router, prefix="/questions", tags=["questions"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])

@app.get("/health", summary="Health Check", description="Checks and returns the current health status of the API.")
async def health_check():
    return {"status": "API is healthy"}
