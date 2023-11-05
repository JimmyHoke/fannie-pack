from typing import Union
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/stats")
def get_posts():
    return {"Hello": "World"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080)