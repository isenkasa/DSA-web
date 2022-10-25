from fastapi import APIRouter

router = APIRouter(
    prefix = "/heap",
    tags = ["heap"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["heap"])
async def root():
    return {"description": "Heap API"}