
import pytest
from httpx import AsyncClient
from src.database import engine, Base
from src.main import app as fastapi_app


@pytest.fixture(scope='session', autouse=True)
async def start_test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac
