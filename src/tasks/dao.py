

from src.dao.base import BaseDAO
from src.tasks.models import Tasks



class TaskDAO(BaseDAO):
    model = Tasks