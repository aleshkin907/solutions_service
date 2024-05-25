from pydantic import BaseModel


class ResponseSolutionSchema(BaseModel):
    id: str
    user_id: str
    task_id: str
    status: str
    solution: str
    traceback: str

class RequestSolutionSchema(BaseModel):
    topic: str
    user_id: str
    task_id: str
    solution: str
    unit_test: str

class SolutionSchema(BaseModel):
    user_id: str
    task_id: str
    solution: str
    