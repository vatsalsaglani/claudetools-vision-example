import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from engine import extractContentFromImage

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImageInput(BaseModel):
    image_str: str
    media_type: str


@app.get("/")
async def index():
    return {"ok": True}


@app.post("/api/extract")
async def api_extract(payload: ImageInput):
    return await extractContentFromImage(payload.image_str, payload.media_type)


if __name__ == "__main__":
    uvicorn.run("app:app", port=8890, host="0.0.0.0", reload=True)
