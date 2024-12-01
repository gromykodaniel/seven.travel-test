
from sqlalchemy import CheckConstraint , ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.database import Base


class   Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    status:Mapped[str] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)  # Внешний ключ на таблицу Users

    user: Mapped["Users"] = relationship("Users", back_populates="tasks")

    __table_args__ = (
        CheckConstraint(
            "status IN ('todo', 'in_progress', 'done')",
            name="check_status_valid"
        ),
    )
