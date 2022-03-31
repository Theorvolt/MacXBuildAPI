from fastapi import FastAPI
from server.endpoints import router as Notes

app = FastAPI()

app.include_router(Notes, tags=["Notes"], prefix="/notes")