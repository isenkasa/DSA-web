from fastapi import APIRouter

router = APIRouter(
    prefix = "/dynamic-programming",
    tags = ["dynamic-programming"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["dynamic-programming"])
async def root():
    return {"description": "Dynamic Programming"}