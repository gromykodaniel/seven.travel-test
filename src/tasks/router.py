from fastapi import APIRouter  , Depends , HTTPException
from sqlalchemy import text
from src.database import async_session_maker
from src.tasks.dao import TaskDAO
from src.tasks.schemas import STaskAdd, STaskGet, STaskId, STaskPut
from src.user.auth import get_password_hash , get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post('/')
async def add_tasks(task:STaskAdd  , current_user = Depends(get_current_user)):


    cur =  await TaskDAO.create(title = task.title ,description = task.description ,status = task.status ,user_id = current_user.id   )

    if cur :
        return cur.id
    return HTTPException(status_code=404)

@router.get('/')
async def get_tasks(task: str = 'todo'  ,current_user = Depends(get_current_user)  ) :

    a =  await TaskDAO.read(user_id = current_user.id , status = task )
    return  a

@router.get('/{task_id}/'  ,  response_model =STaskAdd )
async def get_task(id:int ,current_user = Depends(get_current_user)):

    cur_task = (await TaskDAO.read(id=id))[0]

    if cur_task and cur_task.id == current_user.id :

        ans = {
            "title":cur_task.title ,
            "description":cur_task.description ,
            "status" :cur_task.status ,
        }
        return ans
    return HTTPException(status_code=404 , detail='Нет такого айди или она не принадлежит вам')

@router.put('/{task_id}')
async def put_task(task: STaskPut ,current_user = Depends(get_current_user)):

    cur_task = await TaskDAO.read(id = task.id , user_id = current_user.id )

    if cur_task :

        cur = await TaskDAO.update(id = task.id  , title = task.title , description = task.description , status = task.status)

        return {cur}
    return HTTPException(status_code=404, detail='Нет такого айди или она не принадлежит вам')

@router.delete('/{task_id}')
async def delete_task(task:STaskId , current_user = Depends(get_current_user) ):

    cur_task = await TaskDAO.read(id=task.id, user_id=current_user.id)

    if cur_task :

        await TaskDAO.delete(id=task.id, user_id=current_user.id)

    return {}





    