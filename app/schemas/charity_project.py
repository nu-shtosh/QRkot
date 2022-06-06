# app/schemas/charity_project.py
from datetime import datetime, timedelta
from typing import Union

from pydantic import BaseModel, Extra, Field, NonNegativeInt, PositiveInt

CREATE_DATE = (
    datetime.now() + timedelta(minutes=10)
).isoformat(timespec='minutes')

CLOSE_DATE = (
    datetime.now() + timedelta(hours=24)
).isoformat(timespec='minutes')


class CharityProjectBase(BaseModel):
    '''Базовый класс проекта.'''
    name: Union[None, str] = Field(
        None,
        min_length=1,
        max_length=100,
        title='Название проекта',
        example='Название проекта',
    )
    description: Union[None, str] = Field(
        None,
        min_length=1,
        title='Описание',
        example='Описание проекта',
    )
    full_amount: Union[None, PositiveInt] = Field(None, example=100_00)

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    '''Схема создания проекта.'''
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        title='Название проекта',
        example='Название проекта',
    )
    description: str = Field(
        ...,
        min_length=1,
        title='Описание',
        example='Описание проекта',
    )
    full_amount: PositiveInt = Field(..., example=100_000)


class CharityProjectUpdate(CharityProjectBase):
    '''Схема обновления проекта.'''
    pass


class CharityProjectDB(CharityProjectCreate):
    '''Полная схема для ответа.'''
    id: PositiveInt = Field(..., title='ID проекта', example=1)
    invested_amount: NonNegativeInt = Field(
        ...,
        title='Сумма пожертвования',
        example=1_000
    )
    fully_invested: bool = Field(
        ...,
        title='Закрыт ли проект',
        example=True
    )
    create_date: datetime = Field(
        ...,
        title='Дата создания проекта',
        example=CREATE_DATE
    )
    close_date: datetime = Field(
        None,
        title='Дата закрытия проекта',
        example=CLOSE_DATE
    )

    class Config:
        orm_mode = True
