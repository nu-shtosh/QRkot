# app/api/validators.py
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectUpdate

BAD_REQUEST_MESSAGE = 'Проект с таким именем уже существует!'
NOT_FOUND_MESSAGE = 'Проект не найден!'
HAS_INVEST_MESSAGE = 'В проекте еще есть инвестиции!'
CLOSED_PROJECT_MESSAGE = 'Закрытый проект нельзя редактировать!'
FULL_AMOUNT_ERROR = 'Нельзя установить требуемую сумму меньше .'


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    '''Проверяет название проекта на уникальность.'''
    new_project_name = await charity_project_crud.get_project_by_name(
        project_name,
        session
    )
    if new_project_name is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=BAD_REQUEST_MESSAGE,
        )


async def check_project_exist(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    '''Проверяет существует ли проект.'''
    project = await charity_project_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=NOT_FOUND_MESSAGE
        )
    return project


async def check_project_invest(
    project_id: int,
    session: AsyncSession,
) -> CharityProject:
    '''Проверяет внесённую сумму в проекте.'''
    project = await charity_project_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=NOT_FOUND_MESSAGE
        )
    if project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=HAS_INVEST_MESSAGE
        )
    return project


async def check_project_update(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession,
) -> CharityProject:
    '''Только для суперюзеров.
    Редактирование проекта'''
    project = await charity_project_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=NOT_FOUND_MESSAGE
        )
    if project.fully_invested is True:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=CLOSED_PROJECT_MESSAGE
        )
    if (
        obj_in.full_amount and obj_in.full_amount < project.invested_amount
    ):
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=FULL_AMOUNT_ERROR
        )
    return project
