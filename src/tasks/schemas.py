from pydantic import BaseModel
from typing import Literal, Optional


class STaskAdd(BaseModel):
    title: str
    description: str
    status :  Literal["todo", "in_progress", "done"]

class STaskPut(BaseModel):
    id :int
    title: str
    description: str
    status :  Literal["todo", "in_progress", "done"]


class STaskGet(BaseModel):

    status :  Optional[Literal["todo", "in_progress", "done"]]

class STaskId(BaseModel):

    id :  int

