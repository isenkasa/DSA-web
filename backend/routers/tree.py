from fastapi import APIRouter

router = APIRouter(
    prefix = "/tree",
    tags = ["tree"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["tree"])
async def root():
    return {"description": "Tree API"}