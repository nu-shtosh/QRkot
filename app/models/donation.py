# app/models/donation.py
from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import CheckConstraint, Column, ForeignKey, Text

from app.core import db
from app.models.base import AbstractModel


class Donation(db.Base, AbstractModel):
    '''Модель проектов таблицы donation.'''

    __table_args__ = (
        CheckConstraint(
            'full_amount > 0',
            name='Сумма пожертвования должна быть больше 0'
        ),
        CheckConstraint(
            'invested_amount >= 0',
            name='Сумма взятая из пожертвования должна быть больше 0'
        ),
        CheckConstraint(
            'invested_amount <= full_amount',
            name=('Сумма взятая из пожертвования должна быть '
                  'меньше или равна сумме пожертвования')
        )
    )

    user_id = Column(
        GUID,
        ForeignKey('user.id')
    )
    comment = Column(
        Text,
        nullable=True
    )
