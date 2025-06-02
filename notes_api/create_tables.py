from models import Note
from database import Base, engine

Base.metadata.create_all(bind=engine)

print("таблицы созданы")