# app/crud/charity_project.py
from typing import Optional, List, Dict

from sqlalchemy import extract, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDMeetingRoom:
    def get_projects_by_completion_rate(self):
        pass


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
    ) -> List[Dict[str, str]]:
        result = []
        close_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == 1
            ).order_by(
                extract('month', CharityProject.close_date)
            ).order_by(
                extract('year', CharityProject.close_date)
            ).order_by(
                extract('day', CharityProject.close_date)
            )
        )
        projects = close_projects.scalars().all()
        for project in projects:
            time_complete = str(project.close_date - project.create_date)
            table_fields = {
                'name': project.name,
                'time': time_complete,
                'description': project.description
            }
            result.append(table_fields)

        return result


charity_project_crud = CRUDCharityProject(CharityProject)
