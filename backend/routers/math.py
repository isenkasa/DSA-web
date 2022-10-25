from fastapi import APIRouter

router = APIRouter(
    prefix = "/math",
    tags = ["math"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["math"])
async def root():
    return {"description": "Math API"}