from database import engine, Base
from models import User

print("Создание таблиц...")
Base.metadata.create_all(bind=engine)
print("Готово!")