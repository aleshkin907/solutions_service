from repositories.solution_repository import SolutionRepository
from services.solution_service import SolutionService


def solution_service():
    return SolutionService(SolutionRepository)
