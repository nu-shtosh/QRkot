# app/models/base.py
from sqlalchemy import Boolean, Column, DateTime, Integer


class AbstractModel:
    '''Абстрактная модель проектов таблицы .'''

    full_amount = Column(
        Integer,
        nullable=False
    )
    invested_amount = Column(
        Integer,
        nullable=False,
        default=0
    )
    fully_invested = Column(
        Boolean,
        nullable=False,
        default=False,
    )
    create_date = Column(
        DateTime,
        nullable=False
    )
    close_date = Column(
        DateTime,
        nullable=True
    )
