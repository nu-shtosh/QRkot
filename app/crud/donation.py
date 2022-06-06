# app/crud/donation.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.donation import Donation
from app.schemas.user import UserDB


class CRUDDonation(CRUDBase):
    '''Класс CRUD к таблице donation.'''

    async def get_by_user(
            self,
            session: AsyncSession,
            user: UserDB
    ):
        '''Cписок пожертвований пользователя.'''
        donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return donations.scalars().all()


donation_crud = CRUDDonation(Donation)
