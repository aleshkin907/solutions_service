from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import insert

from models.solution import Solution
from db.db import async_session_maker


class AbstractSolutionRepository(ABC):
    @abstractmethod
    async def create(self, solution: dict) -> str:
        raise NotImplementedError()


class SolutionRepository:
    model = Solution
    async def create(self, solution: dict) -> str:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**solution).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return str(res.scalar_one())
        