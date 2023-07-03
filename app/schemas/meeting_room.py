from typing import Optional
from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    '''Основная схема переговорных.'''
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    '''Схема создания объекта переговорных.'''
    name: str = Field(
        ..., max_length=100
    )


class MeetingRoomUpdate(MeetingRoomBase):
    '''Схема обновления объекта переговорных.'''

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


class MeetingRoomDB(MeetingRoomCreate):
    '''Схема запроса объекта из БД.'''
    id: int

    class Config:
        orm_mode = True
