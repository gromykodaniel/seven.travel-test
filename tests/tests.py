import pytest

from httpx import AsyncClient

from src.user.dao import UserDAO

async def test_register( ac: AsyncClient):


    responce = await ac.post(f"/register",

                             data={
        'username':'test11' ,
        'password': 'test11',
    }
    )

    assert responce.status_code == 200

async def test_login( ac: AsyncClient):


    responce = await ac.post(f"/register",

                             data={
        'username':'test11' ,
        'password': 'test11',
    }
    )

    assert responce.status_code == 200


cur_task_id = None

async def test_add_task( ac: AsyncClient):


    responce = await ac.post(f"/tasks",

                             data={
        "title": "test",
        "description": "test",
        "status": "todo",
    }
    )

    global cur_task_id
    cur_task_id = responce

    assert responce.status_code == 200


async def test_add_task( ac: AsyncClient):


    responce = await ac.get("/tasks/{task_id}/?id="+str(cur_task_id))


    assert responce.status_code == 200

async def test_add_task( ac: AsyncClient):


    responce = await ac.get("http://127.0.0.1:8000/tasks/?task=todo"

    )

    assert len(responce) == 1
    assert responce.status_code == 200







