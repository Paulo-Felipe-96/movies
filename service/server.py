from starlette import status
from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK, description="First test endpoint")
async def get_home():
    return {
        "message": "Hello, World!"
    }
