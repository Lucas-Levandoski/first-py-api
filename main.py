from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


class Post(BaseModel):
    test: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hellow Worlds"}


@app.post("/")
async def root(payload: Post):
    print(payload)
    return {"message": "Hellow Worlds"}


# don`t know why we are passing this Body(...), the (...) makes no sense right now
@app.post("/another-post")
async def root(payload: Post = Body(...)):
    print(payload)
    return {"message": "Hellow Worlds"}
