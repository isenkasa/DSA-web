from fastapi import APIRouter

router = APIRouter(
    prefix = "/backtracking",
    tags = ["backtracking"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["backtracking"])
async def root():
    return {"description": "Backtracking API"}