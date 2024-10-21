# Задача "Модели SQLAlchemy":
# База данных и движок:


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine("sqlite3:///taskmanager.db", echo=True)  #движок указав пусть в БД - 'sqlite:///taskmanager.db'
SessionLocal = sessionmaker(bind=engine) # и локальная сессия

class Base(DeclarativeBase): # Создайте базовый класс Base для других моделей, наследуясь от DeclarativeBase
    pass

