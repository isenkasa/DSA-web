from fastapi import APIRouter

router = APIRouter(
    prefix = "/array",
    tags = ["array"],
    responses = {
        404: {"description": "Not found"}
    }
)

def string_to_arr(arr):
    return list(map(int, arr.split(",")))

@router.get("/", tags=["array"])
async def root():
    return {"description": "Array API"}

@router.get("/contains-duplicate/")
async def contains_duplicate(arr: str):
    arr = string_to_arr(arr)
    hashset = set()
    for n in arr:
        if n in hashset:
            return True
        hashset.add(n)
    return False