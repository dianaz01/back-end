from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Note
from schemas import NoteCreate, NoteOut

app = FastAPI()

# Получаем сессию базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /notes — создаёт заметку
@app.post("/notes", response_model=NoteOut)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(text=note.text)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# GET /notes — возвращает все заметки
@app.get("/notes", response_model=list[NoteOut])
def read_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()