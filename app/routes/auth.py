from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.core.security import create_access_token

router = APIRouter()

class LoginRequest(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=1, max_length=100)

@router.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "password123":
        token = create_access_token(subject=data.username)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")