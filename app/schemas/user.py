# app/schemas/user.py
from fastapi_users import models


class User(models.BaseUser):
    '''Базовая схема юзера.'''
    pass


class UserCreate(models.BaseUserCreate):
    '''Схема для создания юзера.'''
    pass


class UserUpdate(models.BaseUserUpdate):
    '''Схема для обновления юзера.'''
    pass


class UserDB(User, models.BaseUserDB):
    '''Схема для записи юзера в БД.'''
    pass
