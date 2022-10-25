from fastapi import APIRouter

router = APIRouter(
    prefix = "/interval",
    tags = ["interval"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["interval"])
async def root():
    return {"description": "Interval API"}