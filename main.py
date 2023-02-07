from fastapi import *
from fastapi.params import Body
from pydantic import BaseModel


class Post(BaseModel):
    test: str


app = FastAPI()

db = [10]


@app.get("/test/{id}")
def root(id: int, response: Response):

    try:
        return {"message": db[id]}
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
        # response.status_code = 404
        # return {"message": "not found"}


@app.post("/")
async def root(payload: Post):
    db.append(int(payload.test))
    return {"message": db}

# don`t know why we are passing this Body(...), the (...) makes no sense right now


@app.post("/another-post")
async def root(payload: Post = Body(...)):
    print(payload)
    return {"message": "Hellow Worlds"}
