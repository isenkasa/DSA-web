from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import array, string, stack, binary_search, linked_list, tree, trie, heap, backtracking, graph, dynamic_programming, greedy, interval, math, bit

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(array.router)
app.include_router(string.router)
app.include_router(stack.router)
app.include_router(binary_search.router)
app.include_router(linked_list.router)
app.include_router(tree.router)
app.include_router(trie.router)
app.include_router(heap.router)
app.include_router(backtracking.router)
app.include_router(graph.router)
app.include_router(dynamic_programming.router)
app.include_router(greedy.router)
app.include_router(interval.router)
app.include_router(math.router)
app.include_router(bit.router)

@app.get("/")
async def root():
    return {"description": "Data Structures and Algorithms API"}