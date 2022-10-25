from fastapi import APIRouter

router = APIRouter(
    prefix = "/greedy",
    tags = ["greedy"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["greedy"])
async def root():
    return {"description": "Greedy Algorithms API"}