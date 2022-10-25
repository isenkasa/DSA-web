from fastapi import APIRouter

router = APIRouter(
    prefix = "/bit",
    tags = ["bit"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["bit"])
async def root():
    return {"description": "Bit Manipulation API"}