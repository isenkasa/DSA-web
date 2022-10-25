from fastapi import APIRouter

router = APIRouter(
    prefix = "/stack",
    tags = ["stack"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["stack"])
async def root():
    return {"description": "Stack API"}