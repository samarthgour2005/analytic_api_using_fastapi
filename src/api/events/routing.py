from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from api.db.session import get_session
from .models import (
    Eventmodel,
    EventsSchemaList,
    EventCreateSchema,
    EventUpdateSchema,
)


router = APIRouter()

@router.get("/",response_model=EventsSchemaList)
def read_events(session:Session=Depends(get_session)) :

    query=select(Eventmodel).order_by(Eventmodel.id.desc())
    results = session.exec(query).all()
    return {
        "res":results,
        "count":len(results)
    }

@router.get("/{event_id}",response_model=Eventmodel) 
def get_event(event_id:int, session:Session=Depends(get_session)):
    query=select(Eventmodel).where(Eventmodel.id==event_id)
    result=session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404, detail="Event not found")
    return result


@router.post("/", response_model=Eventmodel)
def create_event(
        payload: EventCreateSchema,
        session: Session = Depends(get_session)):
    # construct Eventmodel from the validated payload and persist
    obj = Eventmodel(page=payload.page)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
    


@router.put("/{event_id}",response_model=Eventmodel)
def update_event(event_id:int,
                payload:EventUpdateSchema,
                session:Session=Depends(get_session)) :
    query=select(Eventmodel).where(Eventmodel.id==event_id)
    obj=session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")
    data=payload.model_dump()

    for key,value in data.items():
        setattr(obj,key,value)

    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj