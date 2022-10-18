from fastapi import Depends, FastAPI

from .routers import arrays

app = FastAPI()

app.include_router(arrays.router)

@app.get("/")
async def root():
    return {"description": "Data Structures and Algorithms API"}