from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

FAKE_USER = {
    "username": "admin",
    "password": "admin12345_"
}

def verify_user(username: str, password: str) -> bool:
    return username == FAKE_USER["username"] and pwd_context.verify(password, FAKE_USER["password"])