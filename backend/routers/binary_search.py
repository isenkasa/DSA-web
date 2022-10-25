from fastapi import APIRouter

router = APIRouter(
    prefix = "/binary-search",
    tags = ["binary-search"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["binary-search"])
async def root():
    return {"description": "Binary Search API"}