from fastapi import APIRouter

router = APIRouter(
    prefix = "/string",
    tags = ["string"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["string"])
async def root():
    return {"description": "String API"}