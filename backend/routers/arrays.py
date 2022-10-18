from fastapi import APIRouter

router = APIRouter(
    prefix = "/arrays",
    tags = ["arrays"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["arrays"])
async def arrays_api():
    return {"description": "Arrays API"}