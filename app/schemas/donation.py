# app/schemas/donation.py
from datetime import datetime, timedelta
from typing import Union

from pydantic import (UUID4, BaseModel, Extra, Field, NonNegativeInt,
                      PositiveInt)

CREATE_DATE = (
    datetime.now() + timedelta(minutes=10)
).isoformat(timespec='minutes')

CLOSE_DATE = (
    datetime.now() + timedelta(hours=24)
).isoformat(timespec='minutes')


class DonationBaseSchema(BaseModel):
    '''Базовая схема для инвестиций.'''
    full_amount: PositiveInt = Field(
        ...,
        title='Требуемая сумма',
        example=10_000
    )
    comment: Union[None, str] = Field(
        None,
        title='Комментарий',
        example='Комментарий'
    )

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBaseSchema):
    '''Схема для создания инвестиций.'''
    pass


class DonationGetUser(DonationBaseSchema):
    '''Краткая схема для ответа.'''
    id: PositiveInt = Field(..., example=1)
    create_date: datetime = Field(
        ...,
        title='Дата пожертвования',
        example=CREATE_DATE
    )

    class Config:
        orm_mode = True


class DonationDB(DonationGetUser):
    '''Полная схема для ответа.'''
    user_id: UUID4 = Field(
        ...,
        title='Пользователя, сделавшей пожертвование'
    )
    invested_amount: NonNegativeInt = Field(
        ...,
        title='Сумма из пожертвования, которая распределена по проектам',
        example=10_000
    )
    fully_invested: bool = Field(
        ...,
        title='Все ли деньги из пожертвования были переведены в проект'
    )
    close_date: Union[None, datetime] = Field(
        None,
        title='Дата распределения суммы пожертвований по проектам',
        example=CLOSE_DATE
    )
