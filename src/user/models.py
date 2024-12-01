

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.database import Base


class   Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]

    tasks: Mapped[list["Tasks"]] = relationship("Tasks", back_populates="user", cascade="all, delete")

