from fastapi import FastAPI, Depends
from auth import register_user, login_user, get_db
from schemas import UserCreate, UserLogin
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register")
def register(user: UserCreate, db=Depends(get_db)):
    return register_user(user, db)

@app.post("/login")
def login(user: UserLogin, db=Depends(get_db)):
    return login_user(user, db)