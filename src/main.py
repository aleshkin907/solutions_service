from contextlib import asynccontextmanager
from fastapi import FastAPI

from api_vi.solution import router as solution_router
from services.solution_service import producer


@asynccontextmanager
async def lifespan(app: FastAPI):
    await producer.start()
    yield
    await producer.stop()


app = FastAPI(lifespan=lifespan)
app.include_router(solution_router, prefix="/api/v1")
