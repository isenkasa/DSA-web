from fastapi import APIRouter

router = APIRouter(
    prefix = "/graph",
    tags = ["graph"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["graph"])
async def root():
    return {"description": "Graph API"}