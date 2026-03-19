from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, Field
from typing import Optional, Dict
from jose import jwt, JWTError
from app.core.security import SECRET_KEY, ALGORITHM

router = APIRouter()

NOTES: Dict[int, str] = {}
COUNTER = 1

class NoteCreate(BaseModel):
    text: str = Field(min_length=1, max_length=200)

def require_token(authorization: Optional[str]) -> None:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.split(" ", 1)[1]
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("")
def create_note(note: NoteCreate, authorization: Optional[str] = Header(default=None)):
    global COUNTER
    require_token(authorization)
    NOTES[COUNTER] = note.text
    note_id = COUNTER
    COUNTER += 1
    return {"id": note_id, "text": note.text}

@router.get("/{note_id}")
def get_note(note_id: int, authorization: Optional[str] = Header(default=None)):
    require_token(authorization)
    if note_id not in NOTES:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"id": note_id, "text": NOTES[note_id]}

@router.delete("/{note_id}")
def delete_note(note_id: int, authorization: Optional[str] = Header(default=None)):
    require_token(authorization)
    if note_id not in NOTES:
        raise HTTPException(status_code=404, detail="Note not found")
    del NOTES[note_id]
    return {"deleted": True, "id": note_id}