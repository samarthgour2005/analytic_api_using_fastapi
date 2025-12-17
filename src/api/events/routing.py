from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from api.db.session import get_session
from .models import (
    Eventmodel,
    EventsSchemaList,
    EventCreateSchema,
    EventUpdateSchema,
)


router = APIRouter()

@router.get("/")
def read_events() -> EventsSchemaList:
    return EventsSchemaList(res=[Eventmodel(id=1), Eventmodel(id=2)])

@router.get("/{event_id}") 
def get_event(event_id:int) -> Eventmodel :
    return Eventmodel(id=event_id)


@router.post("/", response_model=Eventmodel)
def create_event(
        payload:EventCreateSchema, 
        session: Session = Depends(get_session)):
    # a bunch of items in a table
    data = payload.model_dump() # payload -> dict -> pydantic
    obj = Eventmodel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
    


@router.put("/{event_id}")
def update_event(event_id:int,payload:EventUpdateSchema) ->Eventmodel:

    print(event_id,payload)
    return Eventmodel(id=event_id)