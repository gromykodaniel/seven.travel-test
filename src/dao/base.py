from sqlalchemy import delete, insert, select , update
from sqlalchemy.exc import SQLAlchemyError

from src.database import async_session_maker


class BaseDAO :

    model = None

    @classmethod

    async  def create(cls , **data):

        try:
            query = insert(cls.model).values( **data ).returning(cls.model.id)

            async with async_session_maker() as session:

                res = await session.execute(query)
                await session.commit()
                return res.mappings().one()
        except():
            return {'Error':'Cannot insert data into table'}



    @classmethod
    async def   read(cls , **filters):
        async with async_session_maker() as session:

            query = select(cls.model.__table__.columns).filter_by(**filters)
            res = await session.execute(query)
            return res.mappings().all()



    @classmethod
    async def update(cls , id: int    , title : str  , description : str , status: str ):

        try:

            async with async_session_maker() as session:
                query = update(cls.model).where(cls.model.id == id).values(title=title,description=description,status=status)
                res = await session.execute(query)
                await session.commit()
                return res.mappings()
        except():
            return {'Error':'Cannot update data into table'}


    @classmethod
    async def delete(cls , **filters):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filters)
            await session.execute(query)
            await session.commit()