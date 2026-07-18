import pytest
from httpx import AsyncClient


async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post("/post", json={"body": body})
    return response.json()



@pytest.fixture()
async def created_post(async_client: AsyncClient):
    return await async_client.post("Test Post", async_client)

@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    name = "Test Post"
    
    response = await async_client .post(
        "/post", 
        json={"body": name}
        )
    
    assert response.status_code == 200
    assert {"id": 0, "body": name}.items() <= response.json().items()