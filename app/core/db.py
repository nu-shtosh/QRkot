# app/core/db.py
from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    '''Подготовительный класс для ORM-моделей.'''
    id = Column(Integer, primary_key=True)  # ой, извеняюсь(

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    '''Генератор объектов сессий подключения к БД.'''
    async with AsyncSessionLocal() as async_session:
        yield async_session
