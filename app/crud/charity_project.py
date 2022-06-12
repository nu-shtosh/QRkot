# app/crud/charity_project.py
from typing import List, Optional

from sqlalchemy import extract, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectShort


class CRUDCharityProject(CRUDBase):
    '''Класс CRUD к таблице charityproject.'''

    async def get_project_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        project_name = await session.execute(
            select(CharityProject).where(
                CharityProject.name == project_name
            )
        )
        project_name = project_name.scalars().first()
        return project_name

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession,
    ) -> List[CharityProjectShort]:
        close_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            ).order_by(
                extract('month', CharityProject.create_date) -
                extract('month', CharityProject.close_date),
                extract('year', CharityProject.create_date) -
                extract('year', CharityProject.close_date),
                extract('day', CharityProject.create_date) -
                extract('day', CharityProject.close_date)
            )
        )
        projects = close_projects.scalars().all()
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)
