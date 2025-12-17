from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI
from api.db.session import init_db
from api.events import router as event_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app startup up
    init_db()
    yield
    # clean up


app = FastAPI(lifespan=lifespan)
app.include_router(event_router,prefix="/api/events")


@app.get("/")
def read_root():
    return {"message": "Hello, damm works!"}

@app.get("/healthz")
def read_root():
    return {"status": "ok"}


