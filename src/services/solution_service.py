from json import dumps
from uuid import UUID

from aiokafka import AIOKafkaProducer

from repositories.solution_repository import AbstractSolutionRepository
from schemas.solution_schema import RequestSolutionSchema, SolutionSchema
from config.config import settings


producer = AIOKafkaProducer(bootstrap_servers=f"{settings.kafka.host}:{settings.kafka.port}")


class SolutionService:
    def __init__(self, solution_repository: AbstractSolutionRepository):
        self.solution_repository: AbstractSolutionRepository = solution_repository()

    async def create(self, solution: RequestSolutionSchema) -> str:
        solution_model = SolutionSchema(
            user_id=solution.user_id,
            task_id=solution.task_id,
            solution=solution.solution
        )
        solution_id = await self.solution_repository.create(solution_model.model_dump())

        message = solution.model_dump()
        del message["topic"]
        await producer.send(solution.topic, dumps(message).encode())

        return solution_id
