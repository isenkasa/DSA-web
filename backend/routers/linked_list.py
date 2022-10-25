from fastapi import APIRouter

router = APIRouter(
    prefix = "/linked-list",
    tags = ["linked-list"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["linked-list"])
async def root():
    return {"description": "Linked List API"}