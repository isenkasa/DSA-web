from fastapi import APIRouter

router = APIRouter(
    prefix = "/arrays",
    tags = ["arrays"],
    responses = {
        404: {"description": "Not found"}
    }
)

def string_to_arr(arr):
    return list(map(int, arr.split(",")))

@router.get("/", tags=["arrays"])
async def arrays_api():
    return {"description": "Arrays API"}

@router.get("/contains-duplicate/")
async def contains_duplicate(arr: str):
    arr = string_to_arr(arr)

    hashset = set()

    for n in arr:
        if n in hashset:
            return True
        hashset.add(n)

    return False