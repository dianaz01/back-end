from fastapi import FastAPI, Depends
from auth.auth_utils import register_user, login_user, get_db
from schemas import UserCreate, UserLogin
from database import Base, engine
from sqlalchemy.orm import Session
from fastapi import FastAPI
from auth import routes as auth_routes
from auth.jwt_handler import create_access_token, verify_token

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_routes.router, prefix="/auth")

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

@app.post("/login")
def login(user: UserLogin, db=Depends(get_db)):
    return login_user(user, db)