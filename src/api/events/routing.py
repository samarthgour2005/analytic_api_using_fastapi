from fastapi import APIRouter
from .schemas import EventSchema


router = APIRouter()

@router.get("/")
def read_events():
    return {"eggs": [5, 431, 1]}

@router.get("/{event_id}") 
def get_event(event_id:int) -> EventSchema :
    return {"id":event_id}