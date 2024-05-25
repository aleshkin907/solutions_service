from uuid import UUID
from enum import Enum
import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as sa_Enum

from db.db import Base
from schemas.solution_schema import SolutionSchema


class Status(str, Enum):
    in_progress = "in_progress"
    completed = "completed"
    failed = "failed"


class Solution(Base):
    __tablename__ = "solutions"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[UUID] = mapped_column(nullable=False)
    task_id: Mapped[UUID] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(sa_Enum(Status), default=Status.in_progress)
    solution: Mapped[str] = mapped_column(nullable=False)
    traceback: Mapped[str] = mapped_column(nullable=True)

    def to_read_model(self) -> SolutionSchema:
        return SolutionSchema(
            id=self.id,
            user_id=self.user_id,
            task_id=self.task_id,
            status=self.status,
            solution=self.solution,
            traceback=self.traceback,
        )
    