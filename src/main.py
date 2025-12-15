from fastapi import FastAPI
from api.events import router as events_router

app = FastAPI()
app.include_router(events_router,prefix="/api/events")


@app.get("/")
def read_root():
    return {"message": "Hello, damm works!"}

@app.get("/healthz")
def read_root():
    return {"status": "ok"}


