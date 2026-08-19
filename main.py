import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, world!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


IMAGES = [
    "https://picsum.photos/id/237/400/300",
    "https://picsum.photos/id/1025/400/300",
    "https://picsum.photos/id/1074/400/300",
]


@app.get("/random-image")
def random_image() -> dict[str, str]:
    return {"image": random.choice(IMAGES)}
