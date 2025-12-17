# from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import List


class Eventmodel(SQLModel):
    id: int


class EventsSchemaList(SQLModel):
    res: List[Eventmodel]


class EventCreateSchema(SQLModel):
    page: str


class EventUpdateSchema(SQLModel):
    desc: str