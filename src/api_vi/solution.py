from uuid import UUID
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from api_vi.dependencies import solution_service
from schemas.solution_schema import RequestSolutionSchema
from services.solution_service import SolutionService


router = APIRouter(
    prefix="/solution",
    tags=["solution"]
)

@router.get("/{user_id}/{task_id}")
async def get_solution(user_id: str, task_id: str):
    pass

@router.post("/")
async def post_solution(
    solution: RequestSolutionSchema,
    solution_service: SolutionService = Depends(solution_service)
    ) -> UUID:
    solution_id = await solution_service.create(solution)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"solution_id": solution_id}
    )
