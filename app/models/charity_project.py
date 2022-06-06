# app/models/charity_project.py
from sqlalchemy import CheckConstraint, Column, String, Text

from app.core.db import Base
from app.models.base import AbstractModel


class CharityProject(Base, AbstractModel):
    '''Модель проектов таблицы charityproject.'''

    __table_args__ = (
        CheckConstraint(
            'full_amount > 0',
            name='Сумма пожертвования должна быть больше 0'
        ),
        CheckConstraint(
            'invested_amount >= 0',
            name='Сумма из пожертвования больше 0'
        ),
        CheckConstraint(
            'invested_amount <= full_amount',
            name=('Сумма из пожертвования должна быть '
                  'меньше или равна сумме пожертвования')
        ),
        CheckConstraint(
            'length(name) BETWEEN 1 AND 100',
            name='Допустимая длина строки — от 1 до 100 символов включительно'
        ),
        CheckConstraint(
            'create_date <= close_date',
            name='Дата создания меньше даты закрытия'
        )
    )

    name = Column(
        String(100),
        unique=True,
        nullable=False
    )
    description = Column(
        Text,
        nullable=False
    )
