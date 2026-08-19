from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_random_image() -> None:
    response = client.get("/random-image")

    assert response.status_code == 200
    assert response.json()["image"] in [
        "https://picsum.photos/id/237/400/300",
        "https://picsum.photos/id/1025/400/300",
        "https://picsum.photos/id/1074/400/300",
    ]
