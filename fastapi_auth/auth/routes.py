from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token, verify_token


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

FAKE_USER = {"username": "admin", "password": "admin123"}

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != FAKE_USER["username"] or form_data.password != FAKE_USER["password"]:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type":"bearer"}

@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "This is a protected route", "user": user["sub"]}