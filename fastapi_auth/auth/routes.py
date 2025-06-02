from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth_utils import create_access_token, verify_token, verify_user, get_db


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    print("DEBUG: username =", form_data.username)
    print("DEBUG: password =", form_data.password)

    user = verify_user(form_data.username, form_data.password, db)
    print("DEBUG: user =", user)
    
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type":"bearer"}

@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "This is a protected route", "user": user["sub"]}

@router.get("/debug-users")
def get_all_users(db: Session = Depends(get_db)):
    from models import User  # убедись, что модель доступна
    users = db.query(User).all()
    return [{"id": u.id, "username": u.username} for u in users]