from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


class Post(BaseModel):
    test: str


app = FastAPI()

db = [10]


@app.get("/test/{id}")
async def root(id: int):
    print(id)
    return {"message": "Hellow Worlds"}


@app.post("/")
async def root(payload: Post):
    db.append(int(payload.test))
    return {"message": db}

# don`t know why we are passing this Body(...), the (...) makes no sense right now


@app.post("/another-post")
async def root(payload: Post = Body(...)):
    print(payload)
    return {"message": "Hellow Worlds"}
