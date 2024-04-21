from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy import delete
from sqlalchemy import text  # Import text function
from task2.models import UserDTO, User

Base = declarative_base()

DATABASE_URL = 'sqlite+aiosqlite:///user_db.sqlite'
engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class UsersService:

    def __init__(self, session: AsyncSession = async_session):
        self.session = session

    async def get(self, user_id: int) -> UserDTO | None:
        async with self.session() as session:
            statement = select(User).filter(User.id == user_id)
            result = await session.execute(statement)
            user = result.scalars().first()
            if user:
                return UserDTO.from_orm(user)
            return None

    async def add(self, user: UserDTO):
        async with self.session() as session:
            new_user = User(id=user.id, username=user.username, email=user.email)
            session.add(new_user)
            await session.commit()

    async def destroy(self, user_id: int):
        async with self.session() as session:
            statement = delete(User).where(User.id == user_id)
            await session.execute(statement)
            await session.commit()



if __name__ == "__main__":
    import asyncio

    result = asyncio.run(UsersService.get(1))
    print(result)
