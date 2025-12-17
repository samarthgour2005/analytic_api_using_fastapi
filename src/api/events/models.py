# from pydantic import BaseModel
from datetime import datetime, timezone
import sqlmodel
from sqlmodel import SQLModel, Field
from typing import List, Optional
from timescaledb import TimescaleModel
from timescaledb.utils import get_utc_now

class Eventmodel(TimescaleModel, table=True):
    page: str = Field(index=True) # /about, /contact, # pricing
    user_agent: Optional[str] = Field(default="", index=True) # browser
    ip_address: Optional[str] = Field(default="", index=True)
    referrer: Optional[str] = Field(default="", index=True) 
    session_id: Optional[str] = Field(default=None, index=True)
    duration: Optional[int] = Field(default=0) 

    __chunk_time_interval__ = "INTERVAL 1 day"
    __drop_after__ = "INTERVAL 3 months"



class EventsSchemaList(SQLModel):
    res: List[Eventmodel]
    count: int


class EventCreateSchema(SQLModel):
    page: str


class EventUpdateSchema(SQLModel):
    desc: str