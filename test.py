
import pytest_asyncio
from httpx import AsyncClient
import pytest
from src.main import app as fa
from src.database import engine, Base

@pytest.fixture(scope='session', autouse=True)
async def start_test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
# Фикстура для клиента
@pytest.fixture()
async def ac():
    async with AsyncClient(base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_register(ac: AsyncClient):
    response = await ac.post(
        "/register",
        json={"username": "test11", "password": "test11"}
    )

    assert response.status_code == 200