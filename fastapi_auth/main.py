from fastapi import FastAPI, Depends
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi

from database import Base, engine
from sqlalchemy.orm import Session
from schemas import UserCreate, UserLogin
from auth_utils import register_user, login_user, get_db
from auth import routes as auth_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Auth System",
    swagger_ui_init_oauth={
        "usePkceWithAuthorizationCodeGrant": False
    }
)

app.include_router(auth_routes.router, prefix="/auth")

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user, db)