from sqlalchemy import create_engine, DateTime

from bl.users_dict import users

engine = create_engine("sqlite+pysqlite:///sqlalchemy_testes.db", echo=True)
print(engine)

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.orm import declarative_base, relationship

# Базовый класс для всех моделей
Base = declarative_base()


class Customer(Base):
    __tablename__ = "peopless"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), unique=True, nullable=False)
    surname = Column(String(64), unique=True, nullable=False)
    age = Column(Integer, nullable=False)

    def __str__(self):
        return f"User <id:{self.id}, first_name:{self.first_name}, surname:({self.surname}, age:({self.age})>"


class Actions(Base):
    __tablename__ = "action"

    user_id = Column(Integer, primary_key=True)
    action = Column(String(255), nullable=False)
    date_action = Column(DateTime, nullable=False)

    def __str__(self):
        return self.text

Base.metadata.create_all(engine)
