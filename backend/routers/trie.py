from fastapi import APIRouter

router = APIRouter(
    prefix = "/trie",
    tags = ["trie"],
    responses = {
        404: {"description": "Not found"}
    }
)

@router.get("/", tags=["trie"])
async def root():
    return {"description": "Trie API"}